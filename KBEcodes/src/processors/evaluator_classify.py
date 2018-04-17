import numpy as np
from processors.classify import rel_classify


BATCHSIZE = 1000


class Evaluator(object):
    def __init__(self, metric, nbest=None, filtered=False, whole_graph=None, ent_vocab=None, rel_vocab=None, graph_path=None):
        assert metric in ['mrr', 'hits', 'all'], 'Invalid metric: {}'.format(metric)
        if metric == 'hits':
            assert nbest, 'Please indicate n-best in using hits'
        if filtered:
            assert whole_graph, 'If use filtered metric, Please indicate whole graph'
            self.all_graph = whole_graph
        self.metric = metric
        self.nbest = nbest
        self.filtered = filtered
        self.batchsize = BATCHSIZE
        self.ress = []
        self.id2sub_list = []
        self.id2obj_list = []
        self.sr2o = {}
        self.ro2s = {}
        self.reltypes = rel_classify(ent_vocab, rel_vocab, graph_path)


    def run(self, model, dataset):
        if self.metric == 'mrr':
            res = self.cal_mrr(model, dataset)
        elif self.metric == 'hits':
            res = self.cal_hits(model, dataset, self.nbest)
        else:
            raise NotImplementedError
        self.ress.append(res)
        return res

    def run_all_matric(self, model, dataset):
        """
        calculating MRR, Hits@1,3,10 (raw and filter)
        """
        n_sample = len(dataset)
        sum_rr_raw = 0.
        sum_rr_flt = 0.
        n_corr_h1_raw = 0
        n_corr_h1_flt = 0
        n_corr_h3_raw = 0
        n_corr_h3_flt = 0
        n_corr_h10_raw = 0
        n_corr_h10_flt = 0
        start_id = 0
        # sum_rr_raw_classified = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        # sum_rr_flt_classified = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        # n_corr_h10_raw_classified = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        # n_corr_h3_raw_classified = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        # n_corr_h1_raw_classified = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        n_corr_h10_flt_classified = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        n_corr_h10_flt_classified_inv = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        # n_corr_h3_flt_classified = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        # n_corr_h1_flt_classified = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        # n_rel_num = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        n_rel_num_fil = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}
        n_rel_num_fil_inv = {'1-1':0, '1-n':0, 'n-1':0, 'n-n':0}



        # for sample in dataset.batch_iter(1, rand_flg=False):
        #     sub, rel, obj = sample[0, 0], sample[0, 1], sample[0, 2]
        #     n_rel_num[self.reltypes[rel]] = n_rel_num[self.reltypes[rel]] + 1
        # print(n_rel_num['1-1'], n_rel_num['1-n'], n_rel_num['n-1'], n_rel_num['n-n'])

        for samples in dataset.batch_iter(self.batchsize, rand_flg=False):
            subs, rels, objs = samples[:, 0], samples[:, 1], samples[:, 2]
            ids = np.arange(start_id, start_id+len(samples))

            # search objects
            raw_scores = model.cal_scores(subs, rels)
            raw_ranks = self.cal_rank(raw_scores, objs)
            sum_rr_raw += sum(float(1/rank) for rank in raw_ranks)
            n_corr_h1_raw += sum(1 for rank in raw_ranks if rank <= 1)
            n_corr_h3_raw += sum(1 for rank in raw_ranks if rank <= 3)
            n_corr_h10_raw += sum(1 for rank in raw_ranks if rank <= 10)

            # cnt = 0
            # for rank in raw_ranks:
                # sum_rr_raw_classified[self.reltypes[rels[cnt]]] += float(1/rank)
                # n_corr_h1_raw_classified[self.reltypes[rels[cnt]]] += rank <= 1
                # n_corr_h3_raw_classified[self.reltypes[rels[cnt]]] += rank <= 3
                # n_corr_h10_raw_classified[self.reltypes[rels[cnt]]] += rank <= 10
                # cnt = cnt + 1

            # filter
            if self.filtered:
                flt_scores = self.cal_filtered_score_fast(subs, rels, objs, ids, raw_scores)
                flt_ranks = self.cal_rank(flt_scores, objs)
                sum_rr_flt += sum(float(1/rank) for rank in flt_ranks)
                n_corr_h1_flt += sum(1 for rank in flt_ranks if rank <=1)
                n_corr_h3_flt += sum(1 for rank in flt_ranks if rank <=3)
                n_corr_h10_flt += sum(1 for rank in flt_ranks if rank <=10)

                cnt = 0
                for rank in flt_ranks:
                    # sum_rr_flt_classified[self.reltypes[rels[cnt]]] += float(1/rank)
                    # n_corr_h1_flt_classified[self.reltypes[rels[cnt]]] += rank <= 1
                    # n_corr_h3_flt_classified[self.reltypes[rels[cnt]]] += rank <= 3
                    if rank <= 10:
                        n_corr_h10_flt_classified[self.reltypes[rels[cnt]]] += 1
                    n_rel_num_fil[self.reltypes[rels[cnt]]] +=1
                    cnt = cnt + 1


            # search subjects
            raw_scores_inv = model.cal_scores_inv(rels, objs)
            raw_ranks_inv = self.cal_rank(raw_scores_inv, subs)
            sum_rr_raw += sum(float(1/rank) for rank in raw_ranks_inv)
            n_corr_h1_raw += sum(1 for rank in raw_ranks_inv if rank <= 1)
            n_corr_h3_raw += sum(1 for rank in raw_ranks_inv if rank <= 3)
            n_corr_h10_raw += sum(1 for rank in raw_ranks_inv if rank <= 10)

            # cnt = 0
            # for rank in raw_ranks:
            #     sum_rr_raw_classified[self.type_inv(self.reltypes[rels[cnt]])] += float(1/rank)
            #     n_corr_h1_raw_classified[self.type_inv(self.reltypes[rels[cnt]])] += rank <= 1
            #     n_corr_h3_raw_classified[self.type_inv(self.reltypes[rels[cnt]])] += rank <= 3
            #     n_corr_h10_raw_classified[self.type_inv(self.reltypes[rels[cnt]])] += rank <= 10
            #     cnt = cnt + 1



            # filter
            if self.filtered:
                flt_scores_inv = self.cal_filtered_score_inv_fast(subs, rels, objs, ids, raw_scores_inv)
                flt_ranks_inv = self.cal_rank(flt_scores_inv, subs)
                sum_rr_flt += sum(float(1/rank) for rank in flt_ranks_inv)
                n_corr_h1_flt += sum(1 for rank in flt_ranks_inv if rank <= 1)
                n_corr_h3_flt += sum(1 for rank in flt_ranks_inv if rank <= 3)
                n_corr_h10_flt += sum(1 for rank in flt_ranks_inv if rank <= 10)

                cnt = 0
                for rank in flt_ranks_inv:
                    # sum_rr_flt_classified[self.type_inv(self.reltypes[rels[cnt]])] += float(1/rank)
                    # n_corr_h1_flt_classified[self.type_inv(self.reltypes[rels[cnt]])] += rank <= 1
                    # n_corr_h3_flt_classified[self.type_inv(self.reltypes[rels[cnt]])] += rank <= 3
                    if rank <= 10:
                        n_corr_h10_flt_classified_inv[self.reltypes[rels[cnt]]] += 1
                    n_rel_num_fil_inv[self.reltypes[rels[cnt]]] += 1
                    cnt = cnt + 1


            start_id += len(samples)
        # print(n_rel_num['1-1'], n_rel_num['1-n'], n_rel_num['n-1'], n_rel_num['n-n'])
        print(n_rel_num_fil['1-1'], n_rel_num_fil['1-n'], n_rel_num_fil['n-1'], n_rel_num_fil['n-n'])

        return {'MRR': sum_rr_raw/n_sample/2,
                'Hits@1': n_corr_h1_raw/n_sample/2,
                'Hits@3': n_corr_h3_raw/n_sample/2,
                'Hits@10': n_corr_h10_raw/n_sample/2,
                'MRR(filter)': sum_rr_flt/n_sample/2,
                'Hits@1(filter)': n_corr_h1_flt/n_sample/2,
                'Hits@3(filter)': n_corr_h3_flt/n_sample/2,
                'Hits@10(filter)': n_corr_h10_flt/n_sample/2,

                # 'MRR_1-1': sum_rr_raw_classified['1-1']/n_rel_num['1-1']/2,
                # 'Hits@1_1-1': n_corr_h1_raw_classified['1-1']/n_rel_num['1-1']/2,
                # 'Hits@3_1-1': n_corr_h3_raw_classified['1-1']/n_rel_num['1-1']/2,
                # 'Hits@10_1-1': n_corr_h10_raw_classified['1-1']/n_rel_num['1-1']/2,
                # 'MRR(filter)_1-1': sum_rr_flt_classified['1-1']/n_rel_num['1-1']/2,
                # 'Hits@1(filter)_1-1': n_corr_h1_flt_classified['1-1']/n_rel_num['1-1']/2,
                # 'Hits@3(filter)_1-1': n_corr_h3_flt_classified['1-1']/n_rel_num['1-1']/2,
                'Hits@10(filter)_head_1-1': n_corr_h10_flt_classified['1-1']/n_rel_num_fil['1-1'],
                'Hits@10(filter)_tail_1-1': n_corr_h10_flt_classified_inv['1-1']/n_rel_num_fil_inv['1-1'],

                # 'MRR_1-n': sum_rr_raw_classified['1-n']/n_rel_num['1-n']/2,
                # 'Hits@1_1-n': n_corr_h1_raw_classified['1-n']/n_rel_num['1-n']/2,
                # 'Hits@3_1-n': n_corr_h3_raw_classified['1-n']/n_rel_num['1-n']/2,
                # 'Hits@10_1-n': n_corr_h10_raw_classified['1-n']/n_rel_num['1-n']/2,
                # 'MRR(filter)_1-n': sum_rr_flt_classified['1-n']/n_rel_num['1-n']/2,
                # 'Hits@1(filter)_1-n': n_corr_h1_flt_classified['1-n']/n_rel_num['1-n']/2,
                # 'Hits@3(filter)_1-n': n_corr_h3_flt_classified['1-n']/n_rel_num['1-n']/2,
                'Hits@10(filter)_head_1-n': n_corr_h10_flt_classified['1-n']/n_rel_num_fil['1-n'],
                'Hits@10(filter)_tail_1-n': n_corr_h10_flt_classified_inv['n-1']/n_rel_num_fil_inv['n-1'],

                # 'MRR_n-1': sum_rr_raw_classified['n-1']/n_rel_num['n-1']/2,
                # 'Hits@1_n-1': n_corr_h1_raw_classified['n-1']/n_rel_num['n-1']/2,
                # 'Hits@3_n-1': n_corr_h3_raw_classified['n-1']/n_rel_num['n-1']/2,
                # 'Hits@10_n-1': n_corr_h10_raw_classified['n-1']/n_rel_num['n-1']/2,
                # 'MRR(filter)_n-1': sum_rr_flt_classified['n-1']/n_rel_num['n-1']/2,
                # 'Hits@1(filter)_n-1': n_corr_h1_flt_classified['n-1']/n_rel_num['n-1']/2,
                # 'Hits@3(filter)_n-1': n_corr_h3_flt_classified['n-1']/n_rel_num['n-1']/2,
                'Hits@10(filter)_head_n-1': n_corr_h10_flt_classified['n-1']/n_rel_num_fil['n-1'],
                'Hits@10(filter)_tail_n-1': n_corr_h10_flt_classified_inv['1-n']/n_rel_num_fil_inv['1-n'],

                # 'MRR_n-n': sum_rr_raw_classified['n-n']/n_rel_num['n-n']/2,
                # 'Hits@1_n-n': n_corr_h1_raw_classified['n-n']/n_rel_num['n-n']/2,
                # 'Hits@3_n-n': n_corr_h3_raw_classified['n-n']/n_rel_num['n-n']/2,
                # 'Hits@10_n-n': n_corr_h10_raw_classified['n-n']/n_rel_num['n-n']/2,
                # 'MRR(filter)_n-n': sum_rr_flt_classified['n-n']/n_rel_num['n-n']/2,
                # 'Hits@1(filter)_n-n': n_corr_h1_flt_classified['n-n']/n_rel_num['n-n']/2,
                # 'Hits@3(filter)_n-n': n_corr_h3_flt_classified['n-n']/n_rel_num['n-n']/2,
                'Hits@10(filter)_head_n-n': n_corr_h10_flt_classified['n-n']/n_rel_num_fil['n-n'],
                'Hits@10(filter)_tail_n-n': n_corr_h10_flt_classified_inv['n-n']/n_rel_num_fil_inv['n-n']
                }



    def cal_mrr(self, model, dataset):
        n_sample = len(dataset)
        sum_rr = 0.
        start_id = 0
        for samples in dataset.batch_iter(self.batchsize, rand_flg=False):
            subs, rels, objs = samples[:, 0], samples[:, 1], samples[:, 2]
            ids = np.arange(start_id, start_id+len(samples))
            scores = model.cal_scores(subs, rels)
            if self.filtered:
                scores = self.cal_filtered_score_fast(subs, rels, objs, ids, scores)
            ranks1 = self.cal_rank(scores, objs)

            scores = model.cal_scores_inv(rels, objs)
            if self.filtered:
                scores = self.cal_filtered_score_inv_fast(subs, rels, objs, ids, scores)
            ranks2 = self.cal_rank(scores, subs)
            sum_rr += sum(float(1/rank) for rank in ranks1 + ranks2)
            start_id += len(samples)
        return float(sum_rr/n_sample/2)

    def cal_hits(self, model, dataset, nbest):
        n_sample = len(dataset)
        n_corr = 0
        start_id = 0
        for samples in dataset.batch_iter(self.batchsize, rand_flg=False):
            subs, rels, objs = samples[:, 0], samples[:, 1], samples[:, 2]
            ids = np.arange(start_id, start_id+len(samples))
            scores = model.cal_scores(subs, rels)
            if self.filtered:
                scores = self.cal_filtered_score_fast(subs, rels, objs, ids, scores)
            res = np.flip(np.argsort(scores), 1)[:, :nbest]
            n_corr += sum(1 for i in range(len(objs)) if objs[i] in res[i])

            scores = model.cal_scores_inv(rels, objs)
            if self.filtered:
                scores = self.cal_filtered_score_inv_fast(subs, rels, objs, ids, scores)
            res = np.flip(np.argsort(scores), 1)
            n_corr += sum(1 for i in range(len(subs)) if subs[i] in res[i])
            start_id += len(samples)
        return float(n_corr/n_sample/2)

    def cal_filtered_score_fast(self, subs, rels, objs, ids, raw_scores, metric='sim'):
        assert metric in ['sim', 'dist']
        new_scores = []
        for s, r, o, i, score in zip(subs, rels, objs, ids, raw_scores):
            true_os = self.id2obj_list[i]
            true_os_rm_o = np.delete(true_os, np.where(true_os == o))
            if metric == 'sim':
                score[true_os_rm_o] = -np.inf
            else:
                score[true_os_rm_o] = np.inf
            new_scores.append(score)
        return new_scores

    def cal_filtered_score_inv_fast(self, subs, rels, objs, ids, raw_scores, metric='sim'):
        assert metric in ['sim', 'dist']
        new_scores = []
        for s, r, o, i, score in zip(subs, rels, objs, ids, raw_scores):
            true_ss = self.id2sub_list[i]
            true_ss_rm_s = np.delete(true_ss, np.where(true_ss==s))
            if metric == 'sim':
                score[true_ss_rm_s] = -np.inf
            else:
                score[true_ss_rm_s] = np.inf
            new_scores.append(score)
        return new_scores

    def cal_rank(self, score_mat, ents):
        return [np.sum(score >= score[e]) for score, e in zip(score_mat, ents)]

    def get_best_info(self):
        if self.metric == 'mrr' or self.metric == 'hits' or self.metric == 'acc':  # higher value is better
            best_val = max(self.ress)
        elif self.metric == 'mr':
            best_val = min(self.ress)
        else:
            raise ValueError('Invalid')
        best_epoch = self.ress.index(best_val) + 1
        return best_epoch, best_val

    def prepare_valid(self, dataset):
        for i in range(len(dataset)):
            s, r, o = dataset[i]
            os = self.all_graph.search_obj_id(s, r)
            ss = self.all_graph.search_sub_id(r, o)
            self.id2obj_list.append(os)
            self.id2sub_list.append(ss)
            self.sr2o[(s, r)] = os
            self.ro2s[(r, o)] = ss


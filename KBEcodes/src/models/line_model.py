
from models.base_model import BaseModel
from models.param import LookupParameter
from utils.math_utils import *


class LineModel(BaseModel):
    def __init__(self, **kwargs):
        self.n_entity = kwargs.pop('n_entity')
        self.n_relation = kwargs.pop('n_relation')
        self.dim = kwargs.pop('dim')
        self.margin = kwargs.pop('margin')
        mode = kwargs.pop('mode', 'pairwise')
        if mode == 'pairwise':
            self.compute_gradients = self._pairwisegrads
        elif mode == 'single':
            self.compute_gradients = self._singlegrads
        else:
            raise NotImplementedError

        self.params = {'e': LookupParameter(name='e', shape=(self.n_entity, self.dim)),
                       'r': LookupParameter(name='r', shape=(self.n_relation, self.dim))}

    def _pairwisegrads(self, pos_samples, neg_samples):
        assert pos_samples.shape == neg_samples.shape
        self.prepare()
        p_scores = self.cal_triplet_scores(pos_samples)
        n_scores = self.cal_triplet_scores(neg_samples)

        loss = max_margin(p_scores, n_scores)
        idxs = np.where(loss > 0)[0]
        if len(idxs) != 0:
            # TODO: inefficient calculation
            pos_subs, pos_rels, pos_objs = pos_samples[idxs, 0], pos_samples[idxs, 1], pos_samples[idxs, 2]
            neg_subs, neg_rels, neg_objs = neg_samples[idxs, 0], neg_samples[idxs, 1], neg_samples[idxs, 2]

            p_s_embs = self.pick_ent(pos_subs)
            p_r_embs = self.pick_rel(pos_rels)
            p_o_embs = self.pick_ent(pos_objs)
            n_s_embs = self.pick_ent(neg_subs)
            n_r_embs = self.pick_rel(neg_rels)
            n_o_embs = self.pick_ent(neg_objs)

            _batchsize = len(pos_subs)

            # p_s_grads = np.zeros(np.shape(p_s_embs))
            # p_o_grads = np.zeros(np.shape(p_o_embs))
            # p_r_grads = np.zeros(np.shape(p_r_embs))

            # n_s_grads = np.zeros(np.shape(n_s_embs))
            # n_o_grads = np.zeros(np.shape(n_o_embs))
            # n_r_grads = np.zeros(np.shape(n_r_embs))

            # print(np.shape(np.sum(p_r_embs * p_o_embs, axis = 1)))
            # print('p len', len(pos_subs))
            # print('n len', len(neg_subs))

            p_r_dot_o_mul_r = (np.sum(p_r_embs * p_o_embs, axis = 1) * (p_r_embs.T)).T
            p_r_dot_s_mul_r = (np.sum(p_r_embs * p_s_embs, axis = 1) * (p_r_embs.T)).T
            p_r_dot_o_mul_s = (np.sum(p_r_embs * p_o_embs, axis = 1) * (p_s_embs.T)).T
            p_r_dot_o_mul_o = (np.sum(p_r_embs * p_o_embs, axis = 1) * (p_o_embs.T)).T
            p_r_dot_s_mul_o = (np.sum(p_r_embs * p_s_embs, axis = 1) * (p_o_embs.T)).T
            p_r_dot_s_mul_s = (np.sum(p_r_embs * p_s_embs, axis = 1) * (p_s_embs.T)).T

            n_r_dot_o_mul_r = (np.sum(n_r_embs * n_o_embs, axis = 1) * (n_r_embs.T)).T
            n_r_dot_s_mul_r = (np.sum(n_r_embs * n_s_embs, axis = 1) * (n_r_embs.T)).T
            n_r_dot_o_mul_s = (np.sum(n_r_embs * n_o_embs, axis = 1) * (n_s_embs.T)).T
            n_r_dot_o_mul_o = (np.sum(n_r_embs * n_o_embs, axis = 1) * (n_o_embs.T)).T
            n_r_dot_s_mul_o = (np.sum(n_r_embs * n_s_embs, axis = 1) * (n_o_embs.T)).T
            n_r_dot_s_mul_s = (np.sum(n_r_embs * n_s_embs, axis = 1) * (n_s_embs.T)).T

            p_s_grads = 2 * (p_s_embs - p_o_embs + p_r_dot_o_mul_r - p_r_dot_s_mul_r)
            p_o_grads = 2 * (p_o_embs - p_s_embs - p_r_dot_o_mul_r + p_r_dot_s_mul_r)
            p_r_grads = 2 * (p_r_dot_s_mul_o + p_r_dot_o_mul_s - p_r_dot_s_mul_s - p_r_dot_o_mul_o)

            n_s_grads = -2 * (n_s_embs - n_o_embs + n_r_dot_o_mul_r - n_r_dot_s_mul_r)
            n_o_grads = -2 * (n_o_embs - n_s_embs - n_r_dot_o_mul_r + n_r_dot_s_mul_r)
            n_r_grads = -2 * (n_r_dot_s_mul_o + n_r_dot_o_mul_s - n_r_dot_s_mul_s - n_r_dot_o_mul_o)

            # for i in range(_batchsize):
            #     p_s_grads[i] =2*(p_s_embs[i]-p_o_embs[i]+p_r_embs[i].dot(p_o_embs[i])*p_r_embs[i]-p_r_embs[i].dot(p_s_embs[i])*p_r_embs[i])
            #     p_o_grads[i] = - p_s_grads[i]
            #     p_r_grads[i] = 2 * (p_r_embs[i].dot(p_s_embs[i]) * p_o_embs[i] + p_r_embs[i].dot(p_o_embs[i]) * p_s_embs[i] 
            #         - p_r_embs[i].dot(p_s_embs[i]) * p_s_embs[i] - p_r_embs[i].dot(p_o_embs[i]) * p_o_embs[i])

            #     n_s_grads[i] =-2*(n_s_embs[i]-n_o_embs[i]+n_r_embs[i].dot(n_o_embs[i])*n_r_embs[i]-n_r_embs[i].dot(n_s_embs[i])*n_r_embs[i])
            #     n_o_grads[i] = - n_s_grads[i]
            #     n_r_grads[i] = -2 * (n_r_embs[i].dot(n_s_embs[i]) * n_o_embs[i] + n_r_embs[i].dot(n_o_embs[i]) * n_s_embs[i] 
            #         - n_r_embs[i].dot(n_s_embs[i]) * n_s_embs[i] - n_r_embs[i].dot(n_o_embs[i]) * n_o_embs[i])


            # n_s_grads = np.zeros(np.shape(n_s_embs))
            # n_o_grads = np.zeros(np.shape(n_o_embs))
            # n_r_grads = np.zeros(np.shape(n_r_embs))

            # print('p_s_grads[0] = ', p_s_grads[0])
            # print('p_s_embs[0] = ', p_s_embs[0])
            # print('norm(p_s_embs[0]) = ', np.linalg.norm(p_s_embs[0]))

            # print('p_r_grads[0] = ', p_r_grads[0])
            # print('p_r_embs[0] = ', p_r_embs[0])
            # print('norm(p_r_embs[0]) = ', np.linalg.norm(p_r_embs[0]))

            # print()

            for idx in range(_batchsize):
                self.params['e'].add_grad(pos_subs[idx], p_s_grads[idx])
                self.params['r'].add_grad(pos_rels[idx], p_r_grads[idx])
                self.params['e'].add_grad(pos_objs[idx], p_o_grads[idx])
                self.params['e'].add_grad(neg_subs[idx], n_s_grads[idx])
                self.params['r'].add_grad(neg_rels[idx], n_r_grads[idx])
                self.params['e'].add_grad(neg_objs[idx], n_o_grads[idx])

        else:
            pass

        self.params['e'].finalize()
        self.params['r'].finalize()

        return loss.mean()

    def _singlegrads(self, samples, ys):
        raise NotImplementedError('Only pairwise setting is available')

    def _cal_similarity(self, sub_emb, rel_emb, obj_emb):
        dist = (sub_emb - obj_emb) + (np.sum(rel_emb * (obj_emb - sub_emb), axis = 1) * rel_emb.T).T
        return -np.sum(dist ** 2, axis=1)

    def cal_scores(self, subs, rels):
        _batchsize = len(subs)
        sub_emb = self.pick_ent(subs)
        rel_emb = self.pick_rel(rels)

        # TODO: maybe inefficient. use matrix operation
        score_mat = np.empty((_batchsize, self.n_entity))
        for i in range(_batchsize):
            qs = sub_emb[i] - self.pick_ent(np.arange(self.n_entity))
            score_mat[i] = - np.linalg.norm(qs + np.outer((-qs).dot(rel_emb[i]), (rel_emb[i])), axis=1) ** 2
        return score_mat

    # TODO: this procedure is the same as cal_scores
    def cal_scores_inv(self, rels, objs):
        _batchsize = len(objs)
        sub_emb = self.pick_ent(objs)
        rel_emb = - self.pick_rel(rels)

        # TODO: maybe inefficient. use matrix operation
        score_mat = np.empty((_batchsize, self.n_entity))
        for i in range(_batchsize):
            qs = sub_emb[i] - self.pick_ent(np.arange(self.n_entity))
            score_mat[i] = - np.linalg.norm(qs + np.outer((-qs).dot(rel_emb[i]), (rel_emb[i])), axis=1) ** 2
        return score_mat

    def cal_triplet_scores(self, samples):
        subs, rels, objs = samples[:, 0], samples[:, 1], samples[:, 2]
        sub_emb = self.pick_ent(subs)
        rel_emb = self.pick_rel(rels)
        obj_emb = self.pick_ent(objs)
        return self._cal_similarity(sub_emb, rel_emb, obj_emb)

    def pick_ent(self, ents):
        return self.params['e'].data[ents]

    def pick_rel(self, rels):
        return self.params['r'].data[rels]

    # def normalize(self):
    #     print(type(self.params['r'].data))
    #     for i in range(len(self.params['r'].data)):
    #         self.params['r'][i] = self.params['r'][i] / np.linalg.norm(self.params['r'][i])
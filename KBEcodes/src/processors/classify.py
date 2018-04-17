from utils.dataset import Vocab
def rel_classify(ent_vocab, rel_vocab, dat_path):
	with open(dat_path, "r") as dat_file:
		rel2head = {}
		rel2tail = {}
		for rel in rel_vocab.id2word:
			rel2head[rel] = {}
			rel2tail[rel] = {}

		print("loading triplets")
		for line in dat_file:
			head, rel, tail = line.strip().split('\t')
			if head not in rel2head[rel].keys():
				rel2head[rel][head] = 1
			else:
				rel2head[rel][head] = rel2head[rel][head] + 1
			if tail not in rel2tail[rel].keys():
				rel2tail[rel][tail] = 1
			else:
				rel2tail[rel][tail] = rel2tail[rel][tail] + 1

		print("calculating")
		rel_type = {}
		rnn = 0
		r11 = 0
		r1n = 0
		rn1 = 0
		for rel in rel_vocab.id2word:
			n_tail = 0
			n_head = 0
			for ent in rel2head[rel].keys():
				n_head = n_head + rel2head[rel][ent]
			for ent in rel2tail[rel].keys():
				n_tail = n_tail + rel2tail[rel][ent]
			# heads per tail = # heads / # (tail types)
			# tails per head = # tails / # (head types)
			if len(rel2tail[rel].keys()) == 0:
				hpt = 0
			else:
				hpt = n_head / len(rel2tail[rel].keys())

			if len(rel2head[rel].keys()) == 0:
				tph = 0
			else:
				tph = n_tail / len(rel2head[rel].keys())
				
			# print(rel_vocab.word2id[rel], rel)
			if hpt > 1.5 and tph > 1.5:
				rel_type[rel_vocab.word2id[rel]] = 'n-n'
				rnn = rnn + 1
			elif hpt > 1.5:
				rel_type[rel_vocab.word2id[rel]] = '1-n'
				rn1 = rn1 + 1 
			elif tph > 1.5:
				rel_type[rel_vocab.word2id[rel]] = 'n-1'
				r1n = r1n +1
			else:
				rel_type[rel_vocab.word2id[rel]] = '1-1'
				r11 = r11 + 1
			out_path = "./test.txt"
	return rel_type
			# with open(out_path, "a") as out_file:
			# 	print(rel, rel_type[rel], file = out_file)

		# with open(out_path, "a") as out_file:
		# 	print("n-n", rnn, file=out_file)
		# 	print("1-1", r11, file=out_file)
		# 	print("1-n", r1n, file=out_file)
		# 	print("n-1", rn1, file=out_file)

if __name__ == '__main__':
	ent_path = "../dat/FB15k/train.entlist"
	rel_path = "../dat/FB15k/train.rellist"
	dat_path = "../dat/FB15k/whole.txt"
	print("loading entities & relation")
	ent_vocab = Vocab.load(ent_path)
	rel_vocab = Vocab.load(rel_path)
	rel_type = rel_classify(ent_vocab, rel_vocab, dat_path)
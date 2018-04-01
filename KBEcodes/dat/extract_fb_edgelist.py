triplet_path = "./FB15k/freebase_mtr100_mte100-train.txt"
ent_path = "./FB15k/train.entlist"
export_path = "./FB15k/FB15k.edgelist"
with open(triplet_path, "r") as in_file, open(ent_path, "r") as ent_file , open(export_path, "w") as out_file:
	id2word = []
	word2id = {}
	for line in ent_file:
		word = line.strip()
		if word not in id2word:
			word2id[word] = len(id2word) + 1
			id2word.append(word)
	ent = []
	for line in in_file:
		sub, rel, obj = line.strip().split('\t')
		print(word2id[sub], word2id[obj], file=out_file)
		print(word2id[obj], word2id[sub], file=out_file)
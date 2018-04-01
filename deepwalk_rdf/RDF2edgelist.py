# transmit the RDF into edgelist
import json
RDF_path = "../datasrc/freebase_mtr100_mte100-train.txt"
export_path = "../datasrc/osp_triplet.edgelist"
dict_path = "../datasrc/word2id.json"

with open(RDF_path, 'r') as in_file, open(export_path, 'w') as out_file:
	'''
		transfer nodes and edges into numbers
		different number infers different name, 
		which could be a node or an edge

	'''
	id2word = []
	word2id = {}
	for line in in_file:
		obj, pred, subj = line.strip().split()[:3]
		if obj not in id2word:
			word2id[obj] = len(id2word) + 1;
			id2word.append(obj)
		if pred not in id2word:
			word2id[pred] = len(id2word) + 1;
			id2word.append(pred)
		if subj not in id2word:
			word2id[subj] = len(id2word) + 1;
			id2word.append(subj)
		print(word2id[obj], word2id[subj], word2id[pred], file = out_file)
	json.dump(word2id, open(dict_path, 'w'))

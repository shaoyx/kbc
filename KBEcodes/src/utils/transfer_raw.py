import numpy as np
from math import sqrt
def set_param(mode = 'default'):
	model_name = "FB15K-237.embeddings"
	model_path = "./utils/" + model_name
	print("pretraining model:", model_name)
	ent_embeddings = []
	with open(model_path, "r") as f:
		line = f.readline()
		[ent_total, dim] = list(map(float, line.split()))
		for line in f:
			ent_embeddings.append(list(map(float, line.split())))

	ent_embeddings.sort(key = lambda x: x[0])

	if mode == 'debug':
		pass

	ans = []
	for ent in ent_embeddings:
		temp = np.array(ent[1:])
		ans.append(temp/sqrt(np.sum(temp**2)))
	return np.array(ans)

if __name__ == '__main__':
	set_param(mode = 'debug')
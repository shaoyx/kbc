import numpy as np
from math import sqrt
def set_param(mode = 'default'):
	model_path = "/Users/CaiYaohui/Documents/Lab/KBEcodes/src/utils/wn.embeddings"
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
		# print(ans[len(ans)-1])
	# print(ans[0], ans[1], ans[2])
	return np.array(ans)

if __name__ == '__main__':
	set_param(mode = 'debug')
from math import log
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import_path2 = "./deep_transe_wn_sgd_normalized/log"
import_path1 = "./transe_wn_sgd/log"

def read_loss(path):
	with open(path) as f:
		epoch = 1
		loss = []
		time = []
		for line in f:
			tmp = "training loss in " + str(epoch) + " epoch:"
			if line.find(tmp) > 0:
				loss.append(float(line[line.find(tmp)+len(tmp)+1::]))

				line = f.readline()
				tmp = "training time in " + str(epoch) + " epoch:"
				time.append(float(line[line.find(tmp)+len(tmp)+1::]))

				epoch = epoch+1
	return np.log(np.array(loss))

if __name__ == "__main__":

	log_loss1 = read_loss(import_path1)
	log_loss2 = read_loss(import_path2)

	plt.figure('TransE & deep_TransE')
	plt.xlabel('epoch')
	plt.ylabel('The log of loss function')
	loss1_line, = plt.plot(log_loss1)
	loss2_line, = plt.plot(log_loss2)
	plt.legend(handles = [loss1_line, loss2_line, ], labels = ['TransE', 'deep_TransE'], loc = 'best')

	plt.savefig('TransE v.s. deep_TransE.png', dpi=300)
	plt.show()
	
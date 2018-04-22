import os
import sys
from math import log
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import re

def is_a_new_expr(line):
	return line.startswith("python train.py")

def is_loss_line(line):
	return line.startswith("INFO:root:training loss in")

def parse_loss(line):
	pattern = r'INFO:root:training loss in (\d+) epoch: (\d+\.\d+)'
	res = re.match(pattern, line)
	if res:
		return (int(res.group(1)), float(res.group(2)))
	else:
		print("No match!!!")
		return (-1, 1)

def parse_legend(line):
	signature = line.split()[-1]
	print(signature) #../log/linemodel_fb15k_0.1_sgd
	res = signature.split("_")
	return res[-2] + "_" + res[-1]

def read_loss(path):
	title = "loss_figures"
	losses = []
	legends = []

	legend = ""
	loss = []
	has_parsed = False

	with open(path) as f:	
		for line in f:
			if is_a_new_expr(line):
				if has_parsed:
					legends.append(legend)
					losses.append(np.log(np.array(loss)))
				legend = parse_legend(line)
				loss = []
				has_parsed = True
			elif is_loss_line(line):
				(epoch, l) = parse_loss(line)
				loss.append(l)
				if epoch != len(loss):
					print("inconsistent")
			else:
				pass

	if has_parsed:
		legends.append(legend)
		losses.append(np.log(np.array(loss)))
	return (title, legends, losses)

if __name__ == "__main__":
	path = sys.argv[1]
	(title, legends, log_losses) = read_loss(path)

	plt.figure(title)
	plt.xlabel('epoch')
	plt.ylabel('The log of loss function')
	print(title)
	print(legends)
	print(len(log_losses))
	lines = []
	for loss in log_losses:
		line, = plt.plot(loss)
		lines.append(line)
	plt.legend(handles = lines, labels = legends, loc = 'best')

	plt.savefig(title+'.png', dpi=300)
	plt.show()
	
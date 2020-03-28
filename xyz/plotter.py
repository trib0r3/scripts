#!/usr/bin/python

# created by shead

import sys
import numpy as np
import matplotlib.pyplot as plt
import pylab


"""
USAGE
============

./plotter.py [log]
./plotter.py my_log.log


REQUIRED DEPENDENCIES
============

* Python2
* Matplot http://matplotlib.org/users/installing.html


FILE FORMAT
============

[iteration] [amount_of_cmp] [amount_of_swaps]
...



EXAMPLE FILE
============

10 1 2
20 30 121
"""



def load_data_from_file(filename, data_size, data_cmp, data_swp):
	with open(filename, 'r') as f:
		for line in f:
			raw = line.split()
			data_size.append(int(raw[0]))
			data_cmp.append(int(raw[1]))
			data_swp.append(int(raw[2]))


# func from docs
def autolabel(rects, ax):
	# attach some text labels
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x() + rect.get_width()/2.0, 1.05*height,
				'%d' % int(height),
				ha='center', va='bottom')



def main(argv):
	if len(argv) != 2:
		print 'USAGE: plotter [path_to_log]'
		sys.exit(1)
	
	
	data_size = []
	data_cmp = []
	data_swp = []
	
	load_data_from_file(argv[1], data_size, data_cmp, data_swp)


	# plot	
	N = len(data_size)

	ind = np.arange(N)  # the x locations for the groups
	width = 0.35	   # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, data_cmp, width, color='r')
	rects2 = ax.bar(ind + width, data_swp, width, color='y')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Values')
	
	title = argv[1].split('.')[0]
	ax.set_title(title)
	
	#ax.set_xticks(ind + width)
	#x.set_xticklabels(data_size)

	ax.legend((rects1[0], rects2[0]), ('cmp', 'swp'))


	#autolabel(rects1, ax)
	#autolabel(rects2, ax)

	fname = '%s.png' % (title)
	pylab.savefig(fname, dpi=333)
	print 'Saved to %s' % fname


if __name__ == "__main__":
	main(sys.argv)
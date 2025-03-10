# multiproc_test.py


import random
import multiprocessing


def list_append(count, id, out_list):
	"""
	Creates an empty list and then appends a 
	random number to the list 'count' number
	of times. A quite CPU-bound/heavy operation!
	"""
	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":
	size = 10000000   # Number of random numbers to add
	procs = 2   # Number of processes to create

	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list 
	jobs = []
	for i in range(0, procs):
		out_list = list()
		process = multiprocessing.Process(target=list_append,args=(size, i, out_list))
		jobs.append(process)
                process.start()

#Modified from source: https://www.quantstart.com/articles/Parallelising-Python-with-Threading-and-Multiprocessing
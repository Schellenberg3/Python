from multiprocessing import Process
from threading import Thread
import os
import math
import time

def calc(start, space, process_num):
	for i in range(start, start + space):
		sqrt = math.sqrt(i)
		# print(f'[Process {process_num}] The square root of {i} is {sqrt}')

if __name__ == '__main__':
	space = 1000000  # Must be a large number for the set-up overhead to save time
	processes = []
	threads = []
	
	proc_start = time.perf_counter()
	for i in range(os.cpu_count()):  # prints the number of logical cores
		print('registering process %d' % i)
		start_at = space*i
		processes.append(Process(target=calc, args=((start_at, space, i))))


	for process in processes:
		process.start()

	for process in processes:
		process.join()

	proc_end = time.perf_counter()
	
	print('Done with multiprocess. Starting Threads.')

	thrd_start = time.perf_counter()

	for i in range(os.cpu_count()):
		print('registering thread %d' % i)
		start_at = space*i	
		threads.append(Thread(target=calc, args=((start_at, space, i))))

	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()

	thrd_end = time.perf_counter()

	print('Done with threads. Starting regular.')

	reg_start = time.perf_counter()

	for j in range(os.cpu_count()*space):
		sqrt = math.sqrt(j)
		# Turns out that print() calls take a ton of time to run.
		# print(f'[Regular] The square root of {j} is {sqrt}')
		
	reg_end = time.perf_counter()

	print(f'[Info] Summary: for {os.cpu_count()*space} calculations each... multiprocessing took {proc_end - proc_start} '
		  f'threading took {thrd_end - thrd_start}'
		  f'and regular took {reg_end - reg_start}')

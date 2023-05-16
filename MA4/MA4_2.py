#!/usr/bin/env python3
from person import Person
import matplotlib.pyplot as plt
import numba
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt


@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)
    

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())
        
	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

	#Testing fib_py and fib_numba for n [20,30]
	result_time_py = [] ; result_fib_py = []
	result_time_numba = [] ; result_fib_numba = []
	n = [i for i in range(20, 30, 1)]
	for i in n:
		start = pc()
		result_fib = fib(i)
		end = pc()
		result_time_py.append(end - start)
		start = pc()  
		result_numba = fib_numba(i) 
		end = pc()
		result_time_numba.append(end - start)
        
		result_fib_py.append(result_fib)
		result_fib_numba.append(result_numba)


	plt.plot(n, result_time_py,label='python')
	plt.plot(n, result_time_numba,label='numba')
	plt.xlabel('n')
	plt.ylabel('time')
	plt.legend()
	plt.show()
	plt.savefig('prog2_MA4_plot1.png')	

	n = [i for i in range(30, 45, 1)]
	result_time_py = [] ; result_time_numba = [] ; result_time_cpp = []
	for i in n:
		if i % 3 == 0:
			start = pc()
			result_py = fib(i)
			end = pc()
			result_time_py.append(end - start)
		start = pc()
		result_numba = fib_numba(i)
		end = pc()
		result_time_numba.append(end-start)
		f = Person(i)
		start = pc()
		result_cpp = f.fib()
		end = pc()
		result_time_cpp.append(end-start)

	plt.plot([i for i in n if i%3==0], result_time_py, label='python')
	plt.plot(n, result_time_numba, label='numba')
	plt.plot(n, result_time_cpp, label='c++')
	
	plt.legend()
	plt.xlabel('n')
	plt.ylabel('time')
	plt.savefig('prog2_MA4_plot2.png')



if __name__ == '__main__':
	main()
	


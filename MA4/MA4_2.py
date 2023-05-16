#!/usr/bin/env python3
from person import Person
import matplotlib.pyplot as plt
import numba
from numba import njit


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
	#print(f.getAge())
	#print(f.getDecades())
    #    
	#f.setAge(51)
	#print(f.getAge())
	#print(f.getDecades())

	f.setAge(10)
	print(f.fib())

	f.setAge(40)
	print(f.fib())

if __name__ == '__main__':
	#main()
	


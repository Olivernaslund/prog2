#!/usr/bin/env python3

from person import Person

def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(10)
	print(f.fib())

if __name__ == '__main__':
	main()


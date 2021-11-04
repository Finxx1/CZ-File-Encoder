import os

def compile():
	print('insert file location you want to compile')
	file = input()


	base = os.path.splitext(file)[0]
	os.rename(file, base + '.cz')
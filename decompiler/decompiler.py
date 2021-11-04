import os

def decompile():
	print('insert file location you want to decompile')
	file = input()

	base = os.path.splitext(file)[0]
	os.rename(file, base + '.zip')

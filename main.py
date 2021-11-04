from compiler.compiler import compile
from decompiler.decompiler import decompile

choice = ' '

def start():
	print('compile or decompile?')
	choice = input()
	if choice == 'compile':
		compile()
	else:
		if choice == 'decompile':
			decompile()
		else:
			start()
start()
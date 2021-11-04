from compiler.compiler import compile
from decompiler.decompiler import decompile
from BugCheck.BugChecker import check

choice = ' '

def start():
	print('compile, decompile or bugcheck')
	choice = input()
	if choice == 'compile':
		compile()
	else:
		if choice == 'decompile':
			decompile()
		else:
			if choice == 'bugcheck':
				check()
			else:
				start()
start()

from compiler import compile
from decompiler import decompile

import sys

def start():
    mode = 0
    file_index = 0
    for x in range(len(sys.argv)):
        if sys.argv[x] == 'decompile':
            mode = 1
            file_index = x + 1
        elif sys.argv[x] == 'compile':
            mode = 2
            file_index = x + 1
        elif sys.argv[x] == 'help':
            mode = 3
    if mode == 0:
        print('Use "decompile" to decompile, "compile" to compile, and "help" to display a help menu.')
        sys.exit()
    if mode == 1:
        decompile(sys.argv[file_index])
    if mode == 2:
        for i in range(len(sys.argv) - file_index):
            compile(sys.argv[file_index + i]) 
    if mode == 3:
        print('CZ is a file format that encodes files into a single smaller file.')
        sys.exit()

start()

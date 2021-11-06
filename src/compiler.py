import gzip
import os

def compile(filename):
    filestream = open(filename, "rb")
    filedata = filestream.read()
    filestream.close()
    
    archivename = "archive.cz"
    
    nfiledata = gzip.compress(filedata)
    
    if os.path.exists(filename):
	    nfilestream = open(archivename, "ab")
    else:
	    nfilestream = open(archivename, "wb")
    nfilestream.write(bytes(str(len(str(len(filename)))) + str(len(filename)) + filename + str(len(str(len(nfiledata)))) + str(len(nfiledata)), 'utf-8') + nfiledata)
    nfilestream.close()

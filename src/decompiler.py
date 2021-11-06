import gzip
import os

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def decompile(filename):
    filestream = open(filename, "rb")
    filedata = filestream.read()
    filestream.close()
    
    index = 0
    
    for i in range(len(filedata)):
        i = index
        if i >= len(filedata):
            break;
        print(i)
        nfilenamesizelen = int(str(filedata[i:i + 1])[2:-1])
        nfilenamesize = -1
        nfilenamesize = int(str(filedata[i + 1:i + 1 + nfilenamesizelen])[2:-1])
        nfilename = str(filedata[i + nfilenamesizelen + 1:i + nfilenamesizelen + nfilenamesize + 1])[2:-1]
        nfiledatasizelen = int(str(filedata[i + 1 + nfilenamesize + nfilenamesizelen:i + 1 + nfilenamesize + nfilenamesizelen + 1])[2:-1])
        nfiledatasize = int(str(filedata[i + 1 + nfilenamesizelen + nfilenamesize + 1:i + 1 + nfilenamesizelen + nfilenamesize + 1 + nfiledatasizelen])[2:-1])
        nfiledata = filedata[i + 1 + nfilenamesizelen + nfilenamesize + 1 + nfiledatasizelen:i + 1 + nfilenamesizelen + nfilenamesize + 1 + nfiledatasizelen + nfiledatasize]
        
        nfiledata = gzip.decompress(nfiledata)
        
        nfilestream = open(nfilename, "wb")
        
        nfilestream.write(nfiledata)
        
        index = i + 1 + nfilenamesizelen + nfilenamesize + 1 + nfiledatasizelen + nfiledatasize

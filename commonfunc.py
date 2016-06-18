'''
Created on 18.06.2016

@author: rapnik
'''
import sys
def parseline(lineorig):
    line = lineorig.split()
    valid=True
    path,md5,size =None,None,None
    if (len(line)==3):
        path,md5,size = line
    elif(len(line)>3):
        md5,size = line[-2:]
        path=''
        for part in line[:-2]:
            path+=part+' '
        path = path[:-1]
    else:
        valid=False
        if line:
            print >> sys.stderr, "could not parse line: "+lineorig
    return path,md5,size, valid

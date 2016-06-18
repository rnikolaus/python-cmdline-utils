'''
Created on 18.06.2016

@author: rapnik
'''
import sys
import os
from commonfunc import parseline
from sets import Set
import path



arguments = sys.argv
if len(arguments)<3:
    print 'usage: ',arguments[0],'md5file1','md5file2'
    sys.exit()

def readmd5file(filename):
    md5file={}
    with open(filename , "rb") as f:
        for line in f.readlines():
            
            path,md5,size,valid = parseline(line)
            if not valid:
                continue
            os.path.normpath(path)
            md5file[os.path.normpath(path)]=(md5,size)
        return md5file  

md5file1 = readmd5file(arguments[1])
md5file2 = readmd5file(arguments[2])

set1 = Set(md5file1.keys())
set2 = Set(md5file2.keys())


for path in set1.difference(set2):
    print 'file deleted:',path
    
for path in set2.difference(set1):
    print 'file created:',path
    
for path in set1.intersection(set2):
    if not md5file1[path] == md5file2[path]:
        print 'file changed:',path
    

        



    
    

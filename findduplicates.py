'''
Created on 18.06.2016

@author: rapnik
'''

import sys
from collections import defaultdict
from commonfunc import parseline

vals = defaultdict(list)
for lineorig in sys.stdin:
    
    path,md5,size,valid =parseline(lineorig)
    if not valid:
        continue
    key = str(md5)+'|'+str(size)
    #print key,vals.get(key)
    vals[key].append(path)
for key, value in vals.iteritems():
    if len(value)>1:
        print "duplicate files",value
    

import os
import hashlib
import binascii
import sys
import shutil


buffersize = 4096


dest=None
if len(sys.argv)>2:
    os.chdir(sys.argv[1])
    dest =sys.argv[2]
else:
    print 'usage',sys.argv[0],'sourcepath','destpath'
    sys.exit()

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

    
for path, directories, files in os.walk('.'):
    for filename in files:
        try:
            fullfilename = os.path.join(path,filename)
	    destfile = os.path.join(dest,fullfilename)
	    ensure_dir(destfile)
	    shutil.copy2(fullfilename,destfile)
            
        except IOError as error:
            print >> sys.stderr, error

import os
import hashlib
import binascii
import sys
buffersize = 4096

if len(sys.argv)>1:
    os.chdir(sys.argv[1])
    
for path, directories, files in os.walk('.'):
    for filename in files:
        try:
            fullfilename = os.path.join(path,filename)
            with open(fullfilename , "rb") as f:
                size = os.fstat(f.fileno()).st_size
                m = hashlib.md5()
                byte = f.read(buffersize)
                while len(byte):
                    m.update(byte)
                    byte = f.read(buffersize)
                print unicode(fullfilename),binascii.hexlify(bytearray(m.digest())),size
        except IOError as error:
            print >> sys.stderr, error

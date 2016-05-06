import os
import shutil
from posixpath import join as posix_join, exists as posix_exists, \
    relpath as posix_relpath, normpath as posix_normpath

def copyfiles(dirsrc, dirdst):
    for dirpath, dirnames, filenames in os.walk(dirsrc):
        relpath = posix_relpath(dirpath, dirsrc)
        for dirname in dirnames:
            srcpath = posix_normpath(posix_join(dirpath, dirname))
            dstpath = posix_normpath(posix_join(dirdst, relpath, dirname))
            if not posix_exists(dstpath):
                os.makedirs(dstpath)
        for filename in filenames:
            srcpath = posix_normpath(posix_join(dirpath, filename))
            dstpath = posix_normpath(posix_join(dirdst, relpath, filename))
            if not posix_exists(dstpath):
                shutil.copy(srcpath, dstpath)
                
if '__main__' == __name__:
    copyfiles('./dir0', './dir1')

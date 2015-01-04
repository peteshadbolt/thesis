#!/usr/bin/python

import sys
import anydbm

database_filename='./citefind.db'
texfile='/home/pete/physics/thesis/chapter2/chapter2.tex'
match_db=anydbm.open(database_filename, 'c')

texfile_source=open(texfile, 'r').read()

# print out the match db
print 'Current database:'
for key, value in match_db.items():
    print '%s \t -> \t %s' % (key, value)
    texfile_source=texfile_source.replace(key, value)

new_filename=texfile+'.cited'
f=open(new_filename, 'w')
f.write(texfile_source)
f.close()
print 'wrote %s' % new_filename





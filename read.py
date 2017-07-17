#!/usr/bin/python

#Open a file
fo = open('foo.txt','r+')

# str = fo.read(10);

str = fo.read();

print 'Read string is: ',str

#close opened file

fo.close()

#!/usr/bin/python

#Open a file
fo = open('foo.txt','wb');

print "Name of the file: ",fo.name;
print "Closed or not: ",fo.closed
print "Opening mode: ",fo.mode
print "Softspace flag:",fo.softspace

fo.write("Python is a great language.\nYeah it's great!!\n");

fo.close()

print "Closed or not: ",fo.closed
print "Filename: ",fo.name;

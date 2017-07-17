#!/usr/bin/python


fo = open('foo.txt','r+')

str = fo.read(10);

print "Read string is: ", str



#Check your current location.
position = fo.tell();
print "Current file location : ",position

#Reposition pointer at the beginning once again.

position = fo.seek(0,1);
str = fo.read(10);
print "Again read string: ",str

#Close opened file.
fo.close()

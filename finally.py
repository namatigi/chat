#!/usr/bin/python

try:
    fh= open('testfile',"w")
    fh.write("This is my test goal mfor exception handling.")
finally:
    print "Error: can\'t find file or read data"

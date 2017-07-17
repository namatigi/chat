#!/usr/bin/python


try:
    fh = open('testfile','w')
    try:
        fh.write('This is my test file for this exception')
    finally:
        print "Going to close file"
        fh.close()

except IOError:
    print" Error: can\'t find file or read data"

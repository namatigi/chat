#!/usr/bin/python

#Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError,e:
        print "The argument does not contain numbers\n",e


temp_convert('hello');

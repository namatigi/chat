#!/usr/bin/python


tuple = ( 'abcd',768,2.23, 'john',70.2)

tinytuple = (123,'john')


print tuple

print tuple[0]

print tuple[1:3]

print tuple[2:]

print tinytuple * 2

print tuple + tinytuple


#Invalid operation with tuple
tuple[2] =100; #invalid syntax with tuple

list =['abcd',768,2.23,'john',70.2]

list[2]=100

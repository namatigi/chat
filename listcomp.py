#!/usr/bin/python


nums= [1,2,3,4,5,6]

# mylist= []
#
# for  n in nums:
#     mylist.append(n)
#
# print mylist
#
#
# mylist = [n for n in nums]
# print mylist

# sqr_list = [n*n for n in nums]
#
# print(sqr_list)

#
# mylist = map(lambda n:n*n,nums)
#
# print mylist
#
# mylist =[]
#
# for n in nums:
#     if n%2==0:
#         mylist.append(n)
# print mylist

# mylist = [ n for n in nums if n%2==0]
#
# print mylist
#
# mylist = filter(lambda n:n%2==0,nums)
#
# print mylist

# mylist = []
#
# for letter in 'abcd':
#     for num in range(4):
#         mylist.append((letter,num))
#
# print mylist

mylist = [(letter,num) for letter in 'ABCD' for num in range(4)]

print mylist

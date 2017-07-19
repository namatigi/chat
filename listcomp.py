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

# mylist = [(letter,num) for letter in 'ABCD' for num in range(4)]
#
# print mylist


#DICTIONARY COMPREHENSIONS
# names = ['Bruce','Clark','Peter','Mangu','Paul']
# heros = ['BATMAN','SUPERMAN','SPIDERMAN','WOLVERINE','DEADPOOL']
#
# print zip(names,heros)
#
#
# my_dict = {}
#
# for name,hero in zip(names,heros):
#     my_dict[name] = hero
#
# print my_dict
#
#
# my_dict = {name:hero for name,hero in zip(names,heros) if name !='Peter'}
#
# print my_dict

nums = [1,2,1,3,4,2,4,5,6,7,7,7,8,9,4,5]

my_set =set()

for n in nums:
    my_set.add(n)

print my_set

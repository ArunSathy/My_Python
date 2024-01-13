# l=[1,2,3,'arun','charu']
#
# for i in l:
#     print(i)
#
# print('---------------------','\nIndex : ',l[3])

#---------------------------------------------------------

#adding 2 list elements---------

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=[]
#
# for i in range(len(l1)):
#     l3.append(l1[i]+l2[i])
# print(l3)


#-----------------------------------------------------------

#checking whether the element present in the given list

# l=['mango','orange','kiwi','apple']
#
# x=input('Word : ')
#
# print(x in l)

#-----------------------------------------------------------

#replacing a element in a list

# l=['mango','orange','kiwi','apple']
#
# l[2]='pineapple'
#
# print(l)

#-----------------------------------------------------------

#list functions

# l=['mango','orange','kiwi','apple']

#1. # l.append('pineapple') # inserting an elements into the list at last position
# print(l)

#2. # l.insert(1,'pineapple') # inserting an elements in a specific position
# print(l)

#3. # print(len(l)) # getting the length of the list

#4. # print(l.index('kiwi')) # getting the index position of an element

#--------------------------------------------------------------------------

list=['arun',34,'athira',38,8.9]
list.append('lemon')
list.insert(1,'mango')
list.remove(34)
list.pop()
del list[3:]
list.extend()
print(list)

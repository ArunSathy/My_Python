# set is a collection of unordered and indexed data

# set1={'a','b','c','d'}

# print(set1)

# for i in set1:
#     print(i)

# print('b' in set1)

# set1.add('e') # adding a single element
# print(set1)

# set1.update([1,2,3,4,5]) # adding a set of elements
# print(set1)

# print(len(set1))

# set1.remove('d') # removing an element
# print(set1)

# instead of remove we can use discard

# set1.discard('d')
# print(set1)

# set1.pop() # random element will be removed
# print(set1)

# set1.clear() # clear the all set
# print(set1)

# del set1 # delete the whole set

# set2=set(('a','b','c'))
# print(set2)

#-----union in set-----------

# set2={1,2,4,5}
# set3=set1.union(set2) # combine two sets using union
# set3=set1|set2 # instead of union keyword we can use | symbol
# print(set3)

# set1.update(set2) # can also use
# print(set1)

#----------interference---------------------

# set1={1,3,4,5,6,7,8,}
# set2={2,3,4,0,5,6,7}
#
# set3=set2-set1
# print(set3)

#------------------------------------------

# set1={1,2,9,5,4,1,7,3,8}
# z=(sorted(set1))
# print(z[::-1])

# a={1,2,3,1,3,4,5,6,2,3}
# print(a)
# b={'a','b','c','a'}
# print(b)
#
# print(a|b)
#
#------------------------------------------

# s={'a','b','c','d','e'}
#
# s.add('f')
#
# s.update(['g','h','i'])
#
# s.remove('a')
#
# s.discard('i')
#
# s.clear()
#
# print(s)
#
# print('Length is : ',len(s))

#--------------------------------

# p=set(('a','b','c'))
# print(type(p))

#------------------------------

# s1={'a','b','c'}        # Set union
# s2={1,2,3}
# # s3=s1.union(s2)
# # s3=s1|s2
# print(s3)

#-------------------------------

#set reversing

# l={1,2,3,4,3,2,4,5,6}
# x=(sorted(l))
# print(x[::-1])

s={'a','a','b','c','d','d','c'}
print(s)


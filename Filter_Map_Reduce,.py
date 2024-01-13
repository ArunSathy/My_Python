#---------filter()-----------

# syntax : filter(function,iterables)

# def even(a):
#     return a%2==0
#
# x=[1,2,3,4,5,6,7,8,9]
#
# evens=list(filter(even,x))
#
# print(evens)

#------------------------------

# x=[1,2,3,4,5,6,7,8,9]
#
# evens=list(filter(lambda n: n%2==0,x))  #filter()
# print(evens)

#=========================================

#-------------map()-----------------------

# x=[1,2,3,4,5,6,7,8,9]
#
# evens=tuple(filter(lambda n: n%2==0,x))   #filter()
#
# double=list(map(lambda m:m*2,evens))      #map()
#
# print(double)

#-----------------reduce()------------------------

# from functools import *
#
# x=[1,2,3,4,5,6,7,8,9]
#
# evens=tuple(filter(lambda n: n%2==0,x))   #filter()
#
# double=list(map(lambda m:m*2,evens))      #map()
#
# sum=reduce(lambda a,b:a+b+1,double)         #reduce()
#
# print(evens)
# print(double)
# print(sum)

#----------------------------------------------------------


from functools import *

nums=[1,2,3,4,5,6,7,8,9,10]

evens=list(filter(lambda n:n%2==0,nums))

print('Filter : ',evens)

evens1=list(map(lambda i:i+i,evens))

print('Map    : ',evens1)

evens2=reduce(lambda a,b:a+b,evens)

print('Reduce : ',evens2)














# Arrays are similar to list, but need to have all the values of same type
# when creating an array at the start we have to mention the type code like ; int, float, double

#Refer this youtube video before any interview, it'll be useful for array

# https://www.youtube.com/watch?v=6a39OjkCN5I&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=31



from array import *

# val=array('i',[3,4,5,6,7,4])

# print(val.buffer_info())
# print(val.typecode)
# val.reverse()
# print(val[0])

# for i in range(len(val)):
#     print(val[i])

# different way to print the array one by one

# for i in val:
#     print(i)



#=======================================================

# val=array('u',['a','U','e'])
#
# for i in val:
#     print(i)

#======================================================


# val=array('i',[4,5,6,7,8,9])
#
# new=array(val.typecode,(a for a in val)) # creating a new array with the same type and values of old array
# # new1=array(val.typecode,(a*a for a in val)) # creating new array with the square value of the old array
#
# for i in new:
#     print(i)

#=========================================================

# also doing the same with while loop instead of for loop ( better is for loop )

# val=array('i',[4,5,6,7,8,9])
#
# i=0
# while i<len(val):
#     print(val[i])
#     i+=1

#======================================================

#-----------Array values from user--------------------

# ar=array('i',[])
#
# n=int(input('Enter the Length of the Array : '))
#
# for i in range(n):
#     x=int(input('Enter the values : '))
#     ar.append(x)
#
# print(ar)

# searching the index by getting input value array value from the user

# val=int(input('Enter the value for search : '))
#
# k=0
#
# for e in ar:
#     if e==val:
#         print(k)
#         break
#     k+=1

#===================================================

# ar=array('i',[])
#
# x=int(input('Enter the length of the array : '))
#
# for i in range(x):
#     z=int(input('Enter the values : '))
#     ar.append(z)
#
# print(ar)
#
# m=int(input('Enter the search value : '))
#
# v=0
#
# for e in ar:
#     if e==m:
#         print(v)
#         break
#     v += 1
# else:
#     print('Invalid array value')



#--------------------------------------------------

# print(ar.index(m)) # getting index with the function

#===========================================================

# defautly array doesn't support multidimensional array so we are using Numpy

#---------------------------------------------------------------------------------------

# ay=array('i',[])     #  ay=array('x',[]) || ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d) || so the things in the bracket
#
#
#
# m=int(input('Enter the limit of the array : '))
#
# for i in range(m):
#     z=int(input('Enter the array value : '))
#     ay.append(z)
# print(ay)
#
# n=int(input('Enter the value to find the index : '))
#
# r=0
#
# for j in ay:
#     if j==n:
#         print(r)
#         break
#     r+=1
# else:
#     print('Invalid Index value')



# ar=array('i',[])
#
# limit=int(input('Enter the limit for the array : '))
#
# for i in range(limit):
#     z=int(input('Enter the array value : '))
#     ar.append(z)
#
# print(ar)
#
# random=int(input('Enter the value to find the Index : '))
#
# ind=0
#
# for j in ar:
#     if j==random:
#         print(ind)
#         break
#     ind+=1
# else:
#     print('Invalid Index value')

#---------------------------------------

# val=array('i',[2,3,4,6])

# val.reverse() # reversing the array
# print(val)

# for i in range(len(val)):  # printing the array value according to it's length
#     print(val[i])


# for j in val: # another way for printing the array value according to it's length
#     print(j)


#---------------------------------------------

# v=array('i',[1,2,3,4,5,6])
# # v.reverse()
# # print(v)
#
# for i in v:
#     print(i)

#-----------------------------------------


# arr=array('u',['a','e','i','o','u'])
#
# for i in arr:
#     print(i)

#----------------------------------------


# val=array('i',[2,3,4,6])
#
# newar=array(val.typecode,(a*a for a in val))
#
# for i in newar:
#     print(i)
#
# j=0
# while j<len(val):
#     print(val[j])
#     j+=1

#---------------------------------------


z=array('i',[])

x=int(input('Enter the limit : '))

for i in range(x):
    m=int(input('Enter the value : '))
    z.append(m)
print(z)

n=int(input('Enter the search element : '))

v=0

for j in z:
    if j==n:
        print(v)
        break
    v+=1
else:
    print('Invalid index ')

#------------------------------------------

# v=array('i',[1,2,3,4,5])

# for i in range(len(v)):
#     print(v[i])
#
# print('----------------')
#
# ne=array(v.typecode,(e**2 for e in v)) # deriving a new array with copying old array's type and elements
#
# for j in ne:
#     print(j)

# m=0
# while m<len(v):
#     print(v[m])
#     m+=1

#---------------------------------------------------

# l=[]
#
# m=int(input('Limit : '))
#
# for i in range(m):
#     x=int(input('Enter the value : '))
#     l.append(x)
# print('My list :',l)
#
# n=int(input('Enter the value to find the index : '))
#
# v=0

# for j in l:
#     if n==j:
#         print(v)
#         break
#     v+=1
# else:
#     print('Invalid Index')

# print(l.index(n))  # this is a function which we can use to find the index instead of manual method






























from numpy import *


# ar=array([1,2,3],int)
#
# print(ar)

#===================================

#-------6 ways-----------

# 1. array()

# ar=array([1,2,3,4],)
# print(ar.dtype)
# print(ar)

# 2. linspace()

# ar=linspace(0,10,11)  # the no: is mention the number of parts wanted in the array
# print(ar)

# 3. arange()

# ar=arange(1,10,2) # in this the last no: is mention the steps to be skipped
# print(ar)

# 4.logspace()

# ar=logspace(1,30,3) # this gave the log values and last no: mention is the number of parts wanted in the array
# print('%.2f'%ar[4])

# 5. zeros()

# ar=zeros(5)
# print(ar)

# 6. ones()

# ar=ones(4)
# print(ar)

#===================================================================================

# ar=array([1,2,3,4,5])

#ar=ar*2

#ar=ar+5

# for i in range(len(ar)): # adding into array using for loop
#     ar[i]=i+5
#     print(ar)
# print('---------------')
# print(ar)

# ar1=array([1,2,3,4,5])
# ar2=ar+ar1
# print(ar2)

# print(ar)

# we can use the opertions like : sin, cos, log, min value, max value, sqrt

# ar1=array([2,1,4,3,5])
#
# print(sort(ar1))

# ar1=array([6,7,8,9,10])
#
# print(concatenate([ar,ar1]))

#=====================================================

#----------copying an array-------------

# ar1=ar
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))

#--------------------------------------

# ar1=ar.view()  # using view() function to copy
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))

#--------------------------------------

#---------shallow copy----------


# ar1=ar.view() # view() function is used in shallow copy, both arrays are depended to each others, when one array changes the values it will affect the other array too.
#
# ar[3]=1
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))

#----------deep copy------------


# ar1=ar.copy() # copy() function is used in deep copy, won't affect the second array
#
# ar[3]=1
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))

#-------------------------------------------------


# ar=array([1,2,3,4,5,6])
# print(ar.dtype) # checking the type by using "dtype"
# print(ar)

# ar=linspace(0,15,16)
# print(ar)

# ar=arange(0,16,2)
# print(ar)

# ar=logspace(1,20,5)
# print(ar)
# print('%.2f'%ar[4])

# ar=array([2,3,1,4,5,8,7,6,9])
# print(sort(ar))               # Just sorting the array using a function

# ar=zeros(10)
# print(ar)
#
# ar1=ones(10,int)
# print(ar1)

#-----------------------------------------


# ar=array([1,2,3,4,5])
#
# ar1=array([6,7,8,9,10])

# ar=ar+5
# print(ar)

# print(ar+ar1)

# print(sum(ar1))
#
# print(min(ar))
# print(max(ar1))

# print(concatenate([ar,ar1]))

#---------------------------------------


# ar=array([1,2,3,4,5])
#
# ar1=ar
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))

#---------------------------

# Copying an Array (Shallow copy & Deep Copy


# ar=array([1,2,3,4,5])  #shallow copy | view() function is used |
#
# ar1=ar.view()
#
# ar1[2] = 6
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))

#------------------------------------

# ar=array([1,2,3,4,5]) # deep copy | copy() function is used |
#
# ar1=ar.copy()
#
# ar1[2] = 6
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))


































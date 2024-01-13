from numpy import * # by importing numpy we can create an array without specifying it's type

# Copying an Array (Shallow copy & Deep Copy

#shallow copy ----------------------

# ar=array([1,2,3,4,5])  #shallow copy | view() function is used |
#
# ar1=ar.view()    # by using view() to copy an array, it will change the values of old array
#
# ar1[2] = 6
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))

#------------------------------------

ar=array([11,22,33,44,55])

print(ar)

ar_new=ar.view()

ar_new[2]=66

print(ar)
print(ar_new)


#print('==================================================')

# deep copy ---------------------

# ar=array([1,2,3,4,5]) # deep copy | copy() function is used |
#
# ar1=ar.copy()  # by using copy() to copy an array, it won't change the values of old array
#
# ar1[2] = 6
#
# print(ar)
# print(ar1)
#
# print(id(ar))
# print(id(ar1))

#-------------------------------------

ar=array([11,22,33,44,55])

ar_new=ar.copy()

ar_new[2]=66

print(ar)
print(ar_new)
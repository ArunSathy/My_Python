# Multi Dimensional array

from numpy import *

# ar=array([
#             [1,2,3],
#             [4,5,6],
#             [7,8,9]
#          ])

# print(ar.ndim)  # some operations
# print(ar.shape)
# print(ar.size)

# ar1=ar.flatten() # what ever the dimension is, it will convert into 1 dimensional

#--------------------------------------------------------

# ar1=array([
#             [1,2,3,7,8,9],
#             [4,5,6,1,2,3]
#          ])
#
# ar2=ar1.reshape(4,3)
#
# print(ar2)

#------------------------------------------------------------------

# ar1=array([
#             [1,2,3,7,8,9],
#             [4,5,6,1,2,3]
#          ])
#
# ar2=ar1.reshape(2,2,3)
#
# print(ar2)

#-------------------------------------------------------------------------

#------matrix--------


# ar1=array([
#             [1,2,3,7],
#             [4,5,6,8]
#          ])
#
# # ar2=matrix(ar1)
#
# ar3=matrix('1 2 3 ; 4 5 6 ; 7 8 9') # another way of creating a matrix without any array, only string
# print(ar3)
#
# print(diagonal(ar3)) # to print the diagonal elements in the matrix

#----------multiply 2 matrix----------------

# ar1=matrix('3 1 4')
# ar2=matrix('4 3 ; 2 5 ; 6 8')
#
# ar3=ar1*ar2
# print(ar3)

#---------------------------------------------


# ar=array([
#     [1,2,3,11,12,13],
#     [4,5,6,14,15,16]
#
# ])
#
# ar1=ar.reshape(4,3)
#
# print(ar1)


#------------------------------------------

m=matrix('1 2 3 ; 4 5 6 ; 7 8 9')

n=matrix('1 2 3 ; 4 5 6 ; 7 8 9')

# print(diagonal(m))

# print(m.max(]))

# z=m+n
# print(z)



























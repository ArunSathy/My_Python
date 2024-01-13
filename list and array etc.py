# c=4
# r=5
#
# array= [[1]*c for i in range(r)]
#
# k=0
#
# for i in range(r):      #0-4   0  0  0  0  1  1  1  1  2   2  2  2 3  3  3  3  4  4  4  4
#     for j in range(c):  #0-3   0  1  2  3  0  1  2  3  0   1  2  3 0  1  2  3  0  1  2  3
#         array [i][j]=k  #      00 01 02 03 10 11 12 13 20 21 22 23 30 31 32 33 40 41 42 43
#         k+=1 #
#
# for i in range(r):
#     for j in range(c):
#         s=str(array[i][j])
#         if len(s)==2:
#             print(array[i][j],end="  ")
#         else:
#             print(array[i][j],end="   ")
#     print()

#--------------------myself---------------------------------

# col=4
# row=5
#
# arr = [[4]*col for i in range(row)]
#
# m=0
#
# for i in range(row):
#     for j in range(col):
#         arr [i][j]=m
#         m+=2
#
# for i in range(row):
#     for j in range(col):
#         z=str(arr[i][j])
#         if len(z)==2:
#             print(arr[i][j],end="  ")
#         else:
#             print(arr[i][j],end="   ")
#     print()
#======================================================================

# for i in range(5):     # 0    1   2 2  3 3 3  4 4 4 4
#     for j in range(i): # 0    0   0 1  0 1 2  0 1 2 3
#         print(" *",end=" ")
#     print()

#=====================================================================
#
# for i in range (8):
#     for j in range(i,8-1):
#         print(" ",end=" ")
#     for j  in range(i):
#         print("*",end=" ")
#     print()

#========================================================================

# for i in range(6):
#     for j in range(i):
#         print(" *",end=" ")
#     print()
# for i in range(5):
#     for j in range(i,5-1):
#         print(" *",end=" ")
#     print()
#==========================================================================
# for i in range(6):
#     for j in range(i):
#         print(" ",end="  ")
#     for j in range(i,6):
#         print("*",end="  ")
#     print()


#===========================================================================

# for i in range(6):
#     for j in range(i,6-1):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i-1):
#         print("*",end=" ")
#     print()

# print("=============================================================")
# #
# for i in range(6):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(6,i-1):
#         print("*",end=" ")
#     for j in range(i-1):
#         print("*",end=" ")
#     print()

#======================================================================
# n=int(input("Enter a number : "))
#
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
n=5
#print("================================================")

# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

#print("================================================")

# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

#print("================================================")
#
# for i in range(n):
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i-1):
#         print("*",end=" ")
#     print()
#
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()

#============================================

# for i in range(n-1):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()
#
# for i in range(n):
#     for j in range(i+1,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
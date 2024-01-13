#ASCII CODE
#A-Z   [65-90]
#a-z   [97-122]
#0-9   [48-57]

#==============================================================

n=5
# p=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(p),end=" ")
#     p+=1
#     print()
#
# print("===============================")
#
for i in range(n):
    p = 65
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()
#
# print("===============================")
#
# p=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(p),end=" ")
#         p+=1
#     print()

# print("===============================")
#
# p = 69
# for i in range(n):
#     for j in range(i+1):
#         print(chr(p),end=" ")
#     p-=1
#     print()
#
# p=65
# for i in range(n):
#
#     for j in range(i+1):
#         print(chr(p),end=" ")
#     p+=2
#     print()
#==========================================
#
# for i in range(n):
#     for j in range(i+1):
#         if i%2==0:
#             print("A",end=" ")
#         else:
#             print("B",end=" ")
#     print()
# #
# k=69
#
# for i in range(n):
#     p=k
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(chr(p),end=" ")
#         p-=1
#     k-=1
#     print()

#==================================

# for i in range(n):
#     p=65
#     for j in range(i,n):
#         print(" ",end="  ")
#     for j in range(i):
#         print(chr(p),end="  ")
#         p+=1
#     for j in range(i+1):
#         print(chr(p),end="  ")
#         p-=1
#     print()

#======================================

# s="arun"
# n=len(s)
# p = 0
# for i in range(n):
#     for j in range(i+1):
#         print(s[p],end=" ")
#     p+=1
#     print()

#========================================
# x="PYHTON"
# n=len(x)
# for i in range(n):
#     p=0
#     for j in range(i+1):
#         print(x[p],end="  ")
#         p+=1
#     print()
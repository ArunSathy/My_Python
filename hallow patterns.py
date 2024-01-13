n=5
# for i in range(n):
#     for j in range(n):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#             print("a",end="  ")
#         else:
#             print(" ",end="  ")
#     print()
#
# print("-----------------------------------------------")
#
# for i in range(n):
#     for j in range(n):
#         if(i==j or i+j==n-1):
#             print("a",end="  ")
#         else:
#             print(" ",end="  ")
#     print()
#
# print("-----------------------------------------------")
#
# for i in range(n):
#     for j in range(n):
#         if (i==n//2 or j==n//2):
#             print("a", end="  ")
#         else:
#             print(" ", end="  ")
#     print()

# print("-----------------------------------------------")

# for i in range(n):
#     for j in range(n):
#         if ( i==0 or j==0 or i+j==n-1):
#             print("*",end="  ")
#         else:
#             print(" ",end="  ")
#     print()


for i in range(n):

    for j in range(i,n):
        print(" ",end="  ")

    for j in range(i):
        if (j==0 or i == n-1):
            print("*",end="  ")
        else:
            print(" ",end="  ")

    for j in range(i):
        if (i==n-1 or j==i):
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print()
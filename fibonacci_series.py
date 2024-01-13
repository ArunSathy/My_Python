#fibonacci series

# a,b=0,1
# while a<30:
#     print(a,end=" ")
#     a,b=b,a+b

#---------------------------------------

# a=0
# b=1
# while a<30:
#     print(a,end=" ")
#     a,b=b,a+b

#================================================


# a,b=0,1
#
# while a<30:
#     print(a,end=' ')
#     a,b=b,a+b

#========================================================

# def fibonacci():
#     a,b=0,1
#     while a<20:
#         print(a,end=' ')
#         a,b=b,a+b
#
# fibonacci()

#===========================



# def fib(n):
#     a = 0
#     b = 1
#     print(a,end=' ')
#     print(b,end=' ')
#
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=' ')
#
# n=int(input('Enter the limit : '))
#
# fib(n)

#-------------------------------

# x=int(input('Enter the limit : '))
#
# a,b=0,1
#
# while a<x:
#     print(a, end=' ')
#     a,b=b,a+b

#--------------------------

# n=int(input('Enter the limit : '))

# def fib(n):
#     a,b=0,1
#     print(a,end=' ')
#     print(b,end=' ')
#
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=' ')
# fib(n)

#----------------------------------------

# n=int(input('Enter the limit : '))  # using for loop

# a,b=0,1
# print(a,end=' ')
# print(b,end=' ')

# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=' ')

#-----------------------------

# n=int(input('Enter the limit : ')) # using while loop
#
# a,b=0,1
# while a<n:
#     print(a,end=' ')
#     a,b=b,a+b

#-----------------------------

# n=int(input('Enter the limit : '))  # using for loop  and while loop in function
#
# def fib(n):
#     a=0
#     b=1
#
#     if n<1:
#         print("Invalid input...")
#     elif n==1:
#         print(a)
#     else:
        #----------------------

        # print(a,end=' ')
        # print(b,end=' ')
        #
        # for i in range(n):
        #     c=a+b
        #     a=b
        #     b=c
        #     print(c,end=' ')

        #-----------------------

        # while a<n:
        #     print(a,end=' ')
        #     a,b=b,a+b

        #----------------------
# fib(n)

#---------------------------------------------

n=int(input('Enter the number : '))

def fib(n):
    a = 0
    b = 1
    if n<1:
        print('Invalid input...........')
    elif n==1:
        print(a, end=' ')
    else:

        print(a,end=' ')
        print(b,end=' ')

        for i in range(n):
            c=a+b
            a=b
            b=c
            print(c,end=' ')

fib(n)























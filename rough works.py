# a=[1,2,3,9,5,6]
# print(a(-2,2))
# print(a)
#
# a[3]=4
# print(a)
#
#
# print(a+[7,8,9])
# print(a)
# a.insert(5,1)
# print(a)
# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# a.append(7)
# a.append(4**3)
# print(a)
#
# print(16+16+16+16)
#
# z=['a','b','c','d','e']
# print(z)
# z[1:4]=['B','C','D']
# print(z)
# print(len(z))
#
# q=[3,4,5]
# w=[z,q]
# print(w)
# print(w[0][2])

#fibonacci series
#
# a,b=0,1
# while a<20:
#     print(a,end=" ")
#     a,b=b,a+b

#======================================================================
# n=5
# for i in range(n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# print("-----------------------------------------------")
#
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
#
# print("-----------------------------------------------")
#
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
#
# print("-----------------------------------------------")
#
# for i in range(n+1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


#IF STATEMENT

# x=int(input("enter a number : "))
# if x<0:
#     x=0
#     print("value of x replaced as zero from -ve")
#     print(x)
# elif x==0:
#     print("value of x is zero")
#     print(x)
# elif x==1:
#     print("value of x is one")
#     print(x)
# else:
#     print("value of x is greater one")
#     print(x)

#-----------------------------------------------------------------------
# x=input("Enter your Name : ")
# x=int(input("Enter your  : "))
# if(x%5==0):
#     print("Hello")
# else:
#     print("Bye")


# p = 1
# for i in range(5):
#
#     for j in range(i,5):
#         x=str(p)
#         if len(x)==2:
#             print(p,end=" ")
#         else:
#             print(p,end="  ")
#     p+=1
#     print()


#function with exception question----------------

# def div(a,b):
#     try:
#         z=a//b
#         return z
#     except:
#         print('can\'t divide by zero')
#
#     finally:
#         print('bye')
#
# x=int(input('Enter A : '))
# y=int(input('Enter B : '))
#
# print('Result : ',div(x,y))

#boolean expression-----------------

# a,b=10,5
# print(a>b)
#--------------------------------------

# def div(x,y):
#     try:
#         result=x/y
#     except:
#         print("error")
#     return result
# result=div(10,0)
# print(div(7,0))

#-------------------------------------

# file=open('x.txt','w')
# file.close()

# file=open('x.txt','r')
# x=file.read()
# print(x)
# file.close()

# file=open('x.txt','a')
# file.write("\nI hate my fucking life......")
# file.close()

#------------------------
# a='10'
# print(type(a))
#
# a=1
# a-=1
# print(a)
# a+=1
# print(a)

# print("i hate women")

#------function--------------


# def add(a,b):
#     print(a+b)
# add(3,4)

#function using return

# def sum(x,y):
#     return x+y
# print(sum(3,4))

# print(5%6)

# print(0.1+0.2==0.3)

# a=1
# b=2
#
# print('The value of a is',a,'& the value of b is',b)
#
# print('The value of a is %d & the value of b is %d'%(a,b))

#------------------------------------------------------


# def div(a,b):
#     try:
#         c=a/b
#         print(c)
#     except:
#         print('Can\'t divide by zero')
#     finally:
#         print('Bye')
# x=int(input('Enter A : '))
# y=int(input('Enter B : '))
# div(x,y)

#-----------------------------------------------------


# f=open('demu','w')
# f.write('Hello world')
# f.close()

# f=open('demu','r')
# f1=f.read()
# print(f1)
# f.close()

# f=open('demu','a')
# f.write('\nI\'m Arun Sathyan')







# class A:
#     def mode(self):
#         print('A 1')
#
# class B:
#     def mode(self):
#         print('B 1')
#
# def get(x):
#     x.mode()
#
# a1=A()
# b1=B()

# a1.mode()
# b1.mode()

# get(a1)
# get(b1)

# class IDE1:
#     def ex(self):
#         print('call 1')
#
# class IDE2:
#     def ex(self):
#         print('call 1')
#         print('call 2')
#
#
# def xe(ide):
#     ide.ex()
#
# y=IDE1()
#
# xe(y)


a=2
b=5

a,b=b,a

print('A : ',a,'B : ',b)






















































# class sample:
#     def hello(self,n):
#         print('Hiii......  ',n)
#
# x=sample()
# name='Arun Sathyan'
# x.hello(name)

#--------------------------------------------------------

# class student:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def print(self):
#         print('My name is ',self.name,' and my age is',self.age,', I\'m living in ',self.place)
#
# x=input('Enter your name : ')
# y=int(input('Enter your age : '))
# z=input('Enter you place : ')
#
# o=student(x,y,z)
#
# o.print()

#------------------------------------------------------------

# class cons:
#     def __init__(self):
#         print('hoiiii')
# x=cons()

#==============================================================


# def check():
#     def A():
#         test='A'
#         print('A test value : ',test)
#     def B():
#         nonlocal test
#         test='B'
#     def C():
#         global test
#         test='C'
#
#     test='default'
#     A()
#     print('1st test value :',test)
#     B()
#     print('2nd test value :',test)
#     C()
#     print('3rd test value',test)
#
# check()
# print('outside test value',test)

#===========================================================

# class myclass:
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def details(self):
#         self.name=input('Enter your name : ')
#         self.age=int(input('Enter your age : '))
#
#     def printing(self):
#         print('Name : ',self.name)
#         print('Age  : ',self.age)
#
# x=myclass('','')
#
# x.details()
# x.printing()

#=============================================================

# class sample:
#     def hello(self,name):
#         print('Hello..... ',name)
#     def hi(self,name):
#         print('Hiiii..... ',name)
#
# x=sample()
# x.hello('Arun')
# x.hi('Saranya')

#=============================================================

class sample:
    def hello(self,name):
       self.name=name
    def print(self):
        print(self.name)


x=sample()
name='Arun Sathyan'
x.hello(name)
x.print()

y=sample()
y.hello('Saranya J')
y.print()


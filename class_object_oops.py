# class computer:
#     def config(self):
#         print('i5,16GB,1TB')
#
# hard=computer()
# hard.config()
# computer.config(hard) # another way to call class methods

#-----------------------------------------------------------------

# class computer:
#     def __init__(arun,cpu,ram):
#         arun.cpu=cpu
#         arun.ram=ram
#         print('abcd')
#
#     def get(arun):
#         print('configuration is : ',arun.cpu,' , ',arun.ram)
#
# com=computer('Intel i8','32 GB')
# com.get()

#-------------------------------------------------------------------

#-------constructor----------

# class computer:
#     pass
#
# c=computer
#
# print(id(c))

#==============================================================

# class computer:
#     def __init__(self):
#         self.name="Arun"
#         self.age=25
#
#     def upate(self):
#        self.age=26
#
# obj1=computer()
# obj2=computer()
#
# obj1.name='charutty'
# obj1.age=22
#
# obj1.upate()
#
# print(obj1.name,obj1.age)
# print(obj2.name,obj2.age)

#================================================================

# class computer:
#     def __init__(self):
#         self.name="Arun"
#         self.age=25
#
#     def compare(self,other): # self - obj1 & other - obj2 for the 'if' statement to compare
#         if self.age == other.age:
#             return True
#         else:
#             return False
#
# obj1=computer()
# obj2=computer()
#
# obj1.name='charutty'
# obj1.age=23
#
# # print(obj1.name,obj1.age)
# # print(obj2.name,obj2.age)
#
# if obj1.compare(obj2): # we created the function compare; to compare the age : compare(who is calling, whom to compare)
#     print('they have same age')
# else:
#     print('they don\'t have same age')

#===============================================================================

#---variables------

# types of variable

# 1. Instance variable
# 2. Class (static) variable

# class car:
#
#     wheels=4
#
#     def __init__(self):
#         self.mil=30
#         self.com='BMW'
#
# c1=car()
# c2=car()
#
# c2.com='Audi'
# c2.mil=27
#
# car.wheels=5 # class variable; which is called using class and the values will be changed for all
#
# print(c1.com,c1.mil,c1.wheels)
# print(c2.com,c2.mil,c2.wheels)

#================================================================================

#-------inner class---------

# class student:
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.lap=self.laptop()  # creating object of inner class is in the outer class
#
#     def show(self):
#         print(self.name,self.age)
#         self.lap.show()
#
#     class laptop:
#         def __init__(self):
#             self.brand='Dell'
#             self.cpu='i5'
#             self.ram=8
#
#         def show(self):
#             print(self.brand,self.cpu,self.ram)
#
# s1=student('arun',25,)
# s2=student('saranya',23)
#
# s1.show()

#==========================================================================

# class computer:
#     def __init__(self,ram,cpu):
#         self.r=ram
#         self.c=cpu
#     def data(self):
#         print('Ram : ',self.r,'\nCPU : ',self.c)
#
# o=computer('8 GB','i5 GEN 11')
# o.data()
#
# class A:
#     def main(self):
#         print('Hello All')
#
# x=A()
# A.main(x)

#-------------------------------------------------------------



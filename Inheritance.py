#single inheritance

# class son:
#     def __init__(self,name,dname):
#         self.name=name
#         self.dname = dname
# class dad(son):
#     def get(self):
#         self.name=input("Enter your name : ")
#         self.dname=input("Enter your father's name : ")
#         print("Your name is : ",self.name)
#         print("Your father's name :",self.dname)
# z=dad('','')
# z.get()

#mutlilevel inheritance

# class A:
#     def __init__(self,name,dname):
#         self.name=name
#         self.dname = dname
#
# class B(A):
#     def get(self):
#         self.name=input("Enter your name : ")
#         self.dname=input("Enter your father's name : ")
#         print("Your name is : ",self.name)
#         print("Your father's name :",self.dname)
#
# class C(B):
#     def poc(self):
#         print("ooo llaaaaa")
#
# class D(C):
#     def build(self):
#         print("Hiii llaaaaa")
#
# z=D('','')
# z.get()
# z.poc()
# z.build()

#---------------------------------------------------------------


# class A:
#     def __init__(self,name):
#         self.n=name
#     def A1(self):
#         self.n=input('Enter your Name : ')
# class B(A):
#     def __init__(self,age):
#         self.a=age
#     def B1(self):
#         self.a=int(input('Enter your Age  : '))
#     def data(self):
#         print('Name : ',self.n)
#         print('Age  : ',self.a)
# class C(A):
#     def final(self):
#         print('Bye....Bye.....')
#
# i=B('')
# i.A1()
# i.B1()
# i.data()
#
# o=C('')
# o.final()

#-------------------------------------------

# class A:
#     def __init__(self):
#         print('Parent class')
#     def first(self,name):
#         print('first class')
#         self.n=name
#
# class B():
#     def child_class(self):
#         print('child class')
#     def second(self):
#         print('second class')
#     def display(self):
#         print('Name : ',self.n)
#
# class C(A,B):
#     def final(self):
#         print('final classs')
#
#
# obj=C()
# obj.first('Arun')
# obj.child_class()
# obj.second()
# obj.display()
# obj.final()


#-------------------------------------------

# MRO - Method Resolution Order

# class A:
#     def display(self):
#         print('first')
# class B:
#     def display(self):
#         super().display()
#         print('second')
# class C(B,A):
#     def third(self):
#
#         print('third')
#
# x=C()
# x.display()
# x.third()
#
# print(C.mro())

#----------------------------------------------


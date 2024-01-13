# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.lap=self.Laptop('HP','i5',8)
#
#     def show(self):
#         print('Name : ',self.name)
#         print('Age  : ',self.age)
#         self.lap.show()
#
#     class Laptop:
#         def __init__(self,brand,cpu,ram):
#             self.brand=brand
#             self.cpu=cpu
#             self.ram=ram
#         def show(self):
#             print(self.brand,self.cpu,self.ram)
#
# x=student('arun',25)
# y=student('nura',26)
#
# x.show()
# y.show()

#--------------------------------------------------------

# class company:
#     def __init__(self):
#         print('Outer 1')
#     def show1(self):
#         print('outer 2')
#     class emp:
#         def __init__(self):
#             print('inner 1')
#         def show2(self):
#             print('inner 2')
#
# x=company()
# x.show1()
# y=x.emp()
# y.show2()

# https://www.youtube.com/watch?v=uKl73BWlnyM  --- Reference video for inner class

class A:
    def __init__(self):
        print('init A')

class B:
    def __init__(self):
        print('init B')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('init C')

x=C()

print(C.mro())
# class school:
#     def __init__(self):
#         self.name='arun'
#         self.age=24
#
#     def compare(self,c2):
#         if self.age == c2.age:
#             return True
#         else:
#             return False
#
#
#
#
# c=school()
# c1=school()
# c1.name='athira'
# c1.age=24
#
# if c.compare(c1):
#     print("They are same")
# else:
#     print("they are different")
# print(c.name)
# print(c.age)
# print(c1.name)
# print(c1.age)

#------------------------------------------------

# class A:
#     pass
#
# c1=A()
# c2=A()
#
# print(id(c1))
# print(id(c2))

#------------------------------------------------

# class name:
#     def __init__(self):
#         self.name='Arun'
#         self.age=25
#     def print(self):
#         print(self.name,self.age)
#     def equal(self,a):
#         if self.age==a.age:
#             return True
#         else:
#             return False
#
#
#
# x=name()
# y=name()
#
# y.name='Nura'
# y.age=28
#
# x.print()
# y.print()
#
# if x.equal(y):
#     print('Are equal')
# else:
#     print('Aren\'t equal')

# comparing two objects

class data:
    def __init__(self):
        self.name='Arun'
        self.age=25
    def get_data(self):
        print('Name : ',self.name,'\nAge  : ',self.age)
        print('--------------')
    def equal(self,other):
        if self.age==other.age:
            return True
        else:
            return False
a=data()
b=data()

b.name='Nura'
b.age=27

a.get_data()
b.get_data()

if a.equal(b):
    print('Age is same')
else:
    print('Age isn\'t same')




























# class A:
#     def first(self,name):
#         self.name=name
#
#     def __add__(self, other):
#         s=self.name+other.name
#         return s
#
# n1=A()
# n2=A()
#
# n1.first('Arun ')
# n2.first('Sathyan')
#
# full=n1+n2
# print(full)

#--------------------------------------------

# class A:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#
#     def __str__(self):
#         return ('Measurement : %d length & %d breadth'%(self.l,self.b))
#     def __add__(self, other):
#         return (A(self.l+other.l,self.b+other.b))
#
# m1=A(1,4)
# m2=A(2,5)
# m3=A(3,6)
#
# print(m1+m2+m3)

#---------------------------------------------


# class A:
#     def __init__(self,name):
#         self.name=name
#
#     def __add__(self, other):
#         return (self.name+other.name)
#
# x=A('Arun ')
# y=A('Sathyan')
#
# z=x+y
# print(z)

#----------------------------------------------

# class A:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def __str__(self):
#         return ('Length is : %d cm || Breadth is : %d cm'%(self.l,self.b))
#     def __add__(self, other):
#         return (A(self.l+other.l,self.b+other.b))
#
#
# x=A(1,4)
# y=A(2,5)
# z=A(3,6)
#
# print(x+y+z)

#-----------------------------------------------

class A:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        x=self.m1+other.m1
        y=self.m2+other.m2

        return A(x,y)

    def __gt__(self, other):
        a=self.m1+self.m2
        b=other.m2+other.m2
        if a>b:
            return True
        else:
            return False

    def __str__(self):
        return '{}'.format(self.m1+self.m2)



t1=A(6,2)
t2=A(10,4)

t3=t1+t2

if t1>t2:
    print('first',t1)
else:
    print('second',t2)
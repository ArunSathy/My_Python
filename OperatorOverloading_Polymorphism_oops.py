# x='Mr.'
# y='arun'
# print(x+y)
#
# print(str.__add__(x,y))

#=========================================================

# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#
#     def __add__(self, other):
#         m1=self.m1 + other.m1
#         m2=self.m2 + other.m2
#         s3=student(m1,m2)
#         return s3
#
# s1=student(40,60)
# s2=student(30,40)
# s3 = s1+s2
#
# print(s3.m1)

#==========================================================

# class length:
#     def __init__(self,c,m):
#         self.c=c
#         self.m=m
#     def __str__(self):
#         return ('Length (%d cm, %d mm)' % (self.c,self.m))
#     def __add__(self, other):
#         return (length(self.c+other.c,self.m+other.m))
#
# l1=length(2,6)
# l2=length(5,3)
# l3=length(2,3)
# print(l1+l2+l3)


print(int.__add__(56,10))
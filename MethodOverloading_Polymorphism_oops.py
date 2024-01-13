# class student:
#     def __init__(self,m,n):
#         self.m=m
#         self.n=n
#
#     def sum(self,a=None,b=None,c=None):
#
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#         elif a!=None and b!=None:
#             s=a+b
#         else:
#             s=a
#         return s
#
# z=student()
#
# print(z.sum(3,3))

#----------------------------------------------

class math:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s


z=math()
print(z.sum(11,9,10))
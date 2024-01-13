# class A:
#     __B=0
#
#     def C(self):
#         self.__B+=1
#         print(self.__B)
#
# z=A()
# z.C()
# z.C()
# z.C()
# z.C()
# print(z._A__B)

#-----------------------------------------------------------

# python protects those members by internally changing the name to include the class name.
# you can access such attributes as <<" object._classname__attrName ">>


# Data hiding [Public, Private, Protected]

# a=10    # public    [ can use with in the program ]
# _a=10   # private   [ visible in class and it's subclass ]
# __a=10  # protected [ visible within the class only ]

#------------------------------------------------------------

class counter:
    def __init__(self):
        self._a=5
        self.__b=10

obj=counter()
print(obj._a) # calling a private data
# print(obj.__b)
print(obj._counter__b) # calling a protected data

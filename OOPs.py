# class emp:
#     def __init__(o,name,age): #used 'o' instead of self as the keyword
#         o.x=name # we can give any varible for o.' '=name
#         o.y=age
#     def get(o):
#         o.x=input("Name : ")
#         o.y=input("Age  : ")
#     def give(o):
#         print(o.x,'\n',o.y)
# obj=emp('','')
# obj.get()
# obj.give()

# same program

# class student:
#     def __init__(self, name, age):  #
#         self.name = name  ##--- initailization part
#         self.age = age  #
#
#     def get(self):  # get and put are function, we can give any name for those two
#         self.name = input("Name : ")  # getting inputs
#         self.age = input("Age  : ")  #
#
#     def put(self):
#         print(self.name, '\n', self.age)
#
#
# z = student('', '')  # object can be any variable name
# z.get()
# z.put()


# =============================================================

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get(self):
#         self.name = "Arun"
#         self.age = "24"
#         print(self.name, '\n', self.age) # we can print without creating a new function
#
# z = student('', '')
# z.get()

#----------------------------------------------------

# class com:
#     def con(self):
#         print("arun,athira")
# com1=com()
# com2=com()

# com.con(com1) # not using that oftenly
# com.con(com2)
#both are same ways
# com1.con()
# com2.con()

#----------------------------------------------------

# class com:
#     def con(self):
#         print("arun,athira")
# com1=com()
# com2=com()
#
# com1.con()
# com2.con()

#-------------------------------------------------------

# class computer:
#     def __init__(self,ram,memory):
#         self.ram=ram
#         self.memory=memory
#     def get(self):
#
#         print('Ram is : ',self.ram,'& Memory is : ',self.memory)
#
# config=computer('8 GB  ','1 TB')
# config2=computer('16 GB ','2 TB')
#
# config.get()
# config2.get()


#-----------------------------------------------------------

class memo:
    def hi(self,n):
        print('Hello',n)

x=memo()
ni=' Hi'
x.hi(ni)
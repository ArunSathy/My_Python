
# a=10
#
# def value():
#     # global a
#     a=15
#     print('Local : ',a)
#
# value()
# print('Global : ',a)

#------------replacing the global variable value inside a function using the keyword 'global'------------------

# a=10
# def value1():
#
#     global a # using'global' keyword to change the global variable inside a function
#     a=15
#     print('local 1 : ',a)
#
# def value2():
#     global a
#     a=20
#     print('local 2 : ',a)
#
# def value3():
#     global a
#     a=25
#     print('local 3 : ',a)
#
#
# value1()
# value2()
# value3()
# print('global : ',a)



#---------replacing the global variable value without affecting the local variable using the keyword 'globals'------

# a=10
#
# def value():
#     a=5
#     x=globals()['a']
#     print('Local :',a)
#     # print('value x : ',x)
#     globals()['a']=15
# value()
# print('Global : ',a)

#-------------------------------------------------------------


# x=10
#
# def A():
#     # global x
#     x=15
#     print('local  :',x)
#     globals()['x']=19
#
# A()
#
# print('global :',x)

#---------------------------------------


a=10

def A():

    a=20

    x=globals()['a']
    print('local  : ',a)
    globals()['a']=30

    # print('x initial a value : ',x)

A()
print('global : ',a)








































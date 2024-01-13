#-how ever i divide two numbers; the numerator should be higher value: for that i swapped the numbers

# def div(a,b):
#     if a<b:
#         a,b=b,a
#     return a/b
# print(div(9,3))

#======================================

#------Decorator---------------

# def div(a,b):
#     print(a/b)
#
# def smart(fun):
#     def inside(a,b):
#         if a<b:
#             a,b=b,a
#         return fun(a,b)
#     return inside
#
# div=smart(div)
#
# div(2,4)

#--------------------------------------

def div(a,b):
    print(a//b)

def smart(funct):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return funct(a,b)
    return inner

divi=smart(div)

divi(5,10)

















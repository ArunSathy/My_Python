# x=lambda  a:a+2
# print(x(5))
#
# def add(a):
#     z=a+2
#     return z
# print(add(5))

# x=lambda a,b,c:a+b*c
# print(x(4,5,6))

# x=lambda a,c:a+c
# print(x('arun',' sathyan'))

# def mult(b):
#     return lambda a:a+b
# num=mult(6)
# print(num(6))

# def sub(b):
#     return lambda a:a-b
# new=sub(9)
# print(new(54))

#---------------------------------------------

# x=lambda a,b:a+b
# print(x(2,8))

#----------------------------------

i=int(input('Enter a number : '))

x=lambda a:a**2
print(x(i))

print('-----------')

def add(b):
    y=b**2
    print(y)
add(i)



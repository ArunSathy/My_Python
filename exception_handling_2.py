#-----module-------

# import fibonacci_series
#
# print(fibonacci_series)

#================================================
# a=int(input("enter A : "))
# b=int(input("enter B : "))

# try:
#     z=a//b
#     print(z)
# except:
#     print("can't divide by zero")
# finally:
#     print("Thank you")

#-------------------------------------------------

# def div(a,b):
#     try:
#         z=a//b
#         return z
#     except:
#         print('can\'t divide by zero')
# print('Result : ', div(a, b))

#-----------------------------------------------------

# try:
#     print(a/b)
# except Exception as I:
#     print('sorry, the error is :',I)

# try:
#     print(a//b)
# except:
#     print('sorry')
# finally:
#     print('thank you')

list=[1,2,3,4]
x=int(input('Enter a row : '))
try:
    print(list[x])
except Exception as i:
    print('sorry....!!!,',i)
finally:
    print('come again')
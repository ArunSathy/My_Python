# def div(a,b):
#     print(a/b)
# div(2,0)
#
#----------------------------------------------------
# try:
#     a=int(input("enter a : "))
#     b=int(input("enter b : "))
#     print("\nResult : ",a//b)
#
# except:
#     print("\nSorry, can't perform the operation....")
#
# finally:
#     print("\nThank you :D")
#
#-----------------------------------------------------

# x=int(input("Enter the index : "))
# try:
#     m=[1,2,3,4,5]
#     print("\nThe Element is : ",m[x])
# except:
#     print("\nSorry, element not found in the list...")
# finally:
#     print("\nThank you")

# def div(a,b):
#     try:
#         print(a//b)
#     except Exception as I:
#         if b==0:
#             b=1
#             print('Sorry, we can\'t divide a number by zero so we changed the value of B into 1 & It\'s a',I,'error')
#             print(a//b)
#     finally:
#         print('Work Done...!!!')
# x=int(input('Enter the value of A : '))
# y=int(input('Enter the value of B : '))
# div(x,y)

#-------------------------------------------


z=int(input('enter the index : '))

l=[1,2,3,4]

try:
    print(l[z])
except Exception as i:
    print('sorry',i,'error')
finally:
    print('Thanks')


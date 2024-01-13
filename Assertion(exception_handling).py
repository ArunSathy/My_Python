# z=[2,4,6,8,10,12,3]
#
# for i in z :
#     assert (i%2==0),'odd number'
#
# print(z)


def Age(age):
    assert age>0,'Age cannot be negative'
    print('Age is : ',age)
x=int(input('Enter your age : '))
Age(x)
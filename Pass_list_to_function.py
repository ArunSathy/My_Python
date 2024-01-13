# def count(lst):
#     even=0
#     odd=0
#
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return odd,even
#
# lst=[11,12,13,14,15,16,17,18,19,20]
#
# even,odd=count(lst)
#
# print("Even is : %d & Odd is : %d"%(even,odd))




#========================================

# list=[]
# n=int(input('Enter the list length : '))
#
# for i in range(n):
#     x=input('Enter the Name : ')
#     list.append(x)
# print(list)
#
# def count(list):
#     high=0
#     low=0
#     for i in list:
#         if len(i)>5:
#             high+=1
#         else:
#             low+=1
#     return high,low
#
# list=['arun','athira','charu','pranav','aru']
#
# high,low=count(list)
#
# print("High : %d and Low  : %d"%(high,low))


#---- inserting names into list and finding out the name length--------

# lst=[]
# for i in range(5):
#     x = input("Enter the name : ")
#     lst.append(x)
# def count(lst):
#     greater = 0
#     lesser = 0
#     for i in lst:
#         if len(i) >= 5:
#             greater += 1
#         else:
#             lesser += 1
#     return greater,lesser
# greater,lesser = count(lst)
# print("greater : {} and lesser : {}".format(greater,lesser))


#--------------------------------------------------------

lit=[]

m=int(input('Enter the limit : '))

for i in range(m):
    x=input('Enter the elements : ')
    lit.append(x)
print(lit)

def count(lit):
    even=0
    odd=0
    for i in lit:
        if len(i)>=5:
            even+=1
        else:
            odd+=1
    return even,odd

high,low=count(lit)

print("High : %d and Low  : %d"%(high,low))
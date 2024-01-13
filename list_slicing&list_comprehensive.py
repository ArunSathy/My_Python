#---list slicing-------

# list=[1,2,3,4,5,6,7]
#
# print(list[2:6])
# print(list[:4])
# print(list[3:])
# print(list[::2])

#----list comprehensive-----

# def square():
#     for i in range(10):
#         print(i*i,end=" ")
#
# square()

#using list comprehensive....

# list=[i*i for i in range(10)]
# print('\n',list)

#--------------------------------------------

# m=[]
# for i in "charutty":
#     m.append(i)
# print(m)
#
# z=[x for x in "charutty"]
# print(z)

#----------------------------
# m=[]
# for i in range(10):
#     if i%2==0:
#         m.append(i)
# print(m)

# m=[i for i in range(10) if i%2==0]
# print(m)

#-------------------------------------

# m=[i**2 for i in range(10) if i%2==0]
# print(m)

# x=[]
# for i in "arun":
#     x.append(i)
# print(x)

#-----------------------------------------------
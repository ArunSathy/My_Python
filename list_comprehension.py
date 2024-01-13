# normal function method

# def square():
#     for i in range(10):
#         print(i*i)
# square()

#list comprehensive method

# i=[i*i for i in range(10)]
# print(i)
#----------------------------

# word=[]
# for i in 'arun':
#     word.append(i)
# print(word)
#
# i=[i for i in 'arun']
# print(i)

#-----------------------------------------------

# even=[i for i in range(20) if i%2==0]
# print(even)

# evens=[]
# for i in range(20):
#     if i%2==0:
#         evens.append(i)
# print(evens)

#----------------------------------------------

# m=[1,2,3,4,5,6]
# even=[i**2 for i in m if i%2==0]
# print(even)

#---------------------------------------------

# i=[i*i for i in range(10)]
# print(i)
#
# j=[j**3 for j in range(10)]
# print(j)

#---------------------------------------------


# i=[i for i in 'ARUN']
# print('The Comprehension List : ',i)

# l=[1,2,3,4,5,6,7,8,9,10]
# p=[i**2 for i in l if i>5]
# print(p)


i=[i*2 for i in range(10)]
print(i)

x=lambda a:a*2
print(x(10))


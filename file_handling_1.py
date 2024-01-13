# file=open('arrow.txt','w')
# file.close()

# file=open('arrow.txt','r')
# z=file.read()
# print(z)
# file.close()

# file=open('arrow.txt','a')
# file.write('\nnee shuperdaa')
# file.close()


# file=open('arrow.txt','r+')
# x=file.read()
# print(x)
#
# fp=file.tell()
# print('postion, ',fp)


# file=open('arrow.txt','r')
# z=file.readline()
# z=file.readline()
# z=file.readline()
# print(z)
# file.close()

#-----readline--------

# f=open('arrow.txt','r')
# print(f.readline())

#---------------------------
# f=open('arrow.txt','r')
# for data in f:
#     print(data,end='')
#

# f=open('arrow.txt','r+')
# print('name of the file : ',f.name)

# x=f.readlines()
# print(x)

# l1=f.readline()
# print('read line : ',l1)
# l1=f.readline(5)
# print('read line : ',l1)
# l2=f.readlines()
# print('readlines : ',l2)
# l2=f.readlines(5)
# print('read line : ',l2)
# f.close()

#===========================================================

file=open('python.txt','r')
x=file.readlines()
print(x[1])
file.close()

dic={'a':200,'b':300,'c':400,'d':500,'e':600}
print(dic)
print(dic['a'])
for i in dic.items():
    print(i)
print(dic.values())
print(dic.items())

dic['a']=100
print(dic)
del dic['e']
print(dic)
print(dic['b'])
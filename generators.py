def ten():
    n=1
    while n<=10:
        yield n*n
        n+=1

val=ten()
for i in val:
    print(i)

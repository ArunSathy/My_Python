x=6

for i in range(x):
    for j in range(i):
        print('* ',end=' ')
    print()

print('------------------------------------')

for i in range(x):
    for j in range(i,x-1):
        print('  ',end=' ')
    for j in range(i):
        print('* ',end=' ')
    print()

print('------------------------------------')

for i in range(x):
    for j in range(i,x-1):
        print('* ',end=' ')
    for j in range(i):
        print('  ',end=' ')
    print()

print('------------------------------------')

for i in range(x):
    for j in range(i):
        print('  ',end=' ')
    for j in range(i,x):
        print('* ',end=' ')
    print()

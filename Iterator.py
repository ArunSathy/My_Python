# a=[1,2,3,4,5]
#
# i=iter(a)
#
# print(next(i))

#---------------------

class value:
    def __init__(self):
        self.n=1

    def __iter__(self):
        return self
    def __next__(self):
        if self.n<=10:
            sum=self.n
            self.n+=1
            return sum
        else:
            raise StopIteration
val=value()

print(next(val))

print('-----------')

for i in val:
    print(i)
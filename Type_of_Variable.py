# Instance variable - which defined inside the method
# Class variable - which defined outside the method and inside class


class car:
    tyre=4
    def __init__(self):
        self.mil=23
        self.brand='BMW'

x=car()
y=car()

y.brand='Audi'
y.mil=18

x.tyre=5

print(x.brand,x.mil,x.tyre)
print(y.brand,y.mil,y.tyre)

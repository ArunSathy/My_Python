#Duck Typing

# x = 5
# print(type(x))
#
# x = 'arun'
# print(type(x))

class Duck:
    def sound(self):
        print("Quack Quack")

class Dog():
    def sound(self):
        print('Bark Bark')

class Cat():
    def sound(self):
        print('Meow Meow')

def all_sounds(obj):
    obj.sound()

x=Dog()
all_sounds(x)

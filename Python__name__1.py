# print("Hello "+__name__)


# def fun():
#     print('Hello')
#
# if __name__=="__main__":
#     fun()

#----------------------------------------

# def sum():
#     print('sum calc')
# def sub():
#     print('sub calc')
# def div():
#     print('div calc')
#
# def s():
#     print("calc main")
#     sum()
#     sub()
#     div()
#
# if __name__ == '__main__':
#     s()


#===============================================================================

def add():
    print('Addition')
def sub():
    print('Substraction')
def mult():
    print('Multiplication')
def div():
    print('Division')

def total():
    print('Totally it\'s done',__name__)
    add()
    sub()
    mult()
    div()

if __name__=='__main__':   # __main__ only can be used for this
    total()

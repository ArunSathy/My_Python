# from threading import *
# from time import *
#
# class hello(Thread):
#     def run(self):
#         for i in range(3):
#             print('hello')
#             sleep(1)
# class hi(Thread):
#     def run(self):
#         for i in range(3):
#             print('hi')
#             sleep(1)
#
# o1=hello()
# o2=hi()
#
# o1.start()
# sleep(0.2)
# o2.start()
#
# o1.join()
# o2.join()
#
# print('bye')

#----------------------------------

from threading import *
from time import *

# class A(Thread):
#     def run(self):   # "run" is the only method name which will help to execute when start is called
#         for i in range(5):
#             print('Hi 1')
#             sleep(1)
#
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print('Hello 2')
#             sleep(1)
#
# x=A()
# y=B()
#
# x.start()
# sleep(0.2) # "sleep" is used to make the other threads wait to execute
# y.start()
#
# x.join() # "join" is using to make wait the main thread "print('bye')"
# y.join() # then main thread will only execute after the execution of both the sub threads
#
# print('Bye')

#--------------------------------------------

class A(Thread):
    def run(self):
        for i in range(10):
            print('first 1')
            sleep(1)


class B(Thread):
    def run(self):
        for i in range(10):
            print('second 2')
            sleep(1)

x=A()
y=B()

x.start()
sleep(0.5)
y.start()

x.join()
y.join()

print('bye')







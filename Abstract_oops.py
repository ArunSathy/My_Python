# ABC - Abstract Base Classes

# from abc import ABC, abstractmethod
#
# class computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
#
# class laptop():
#     def process(self):
#         print('calling')
#
# o=computer()
# o1=laptop()
# o1.process()
# o.process()

#=======================================

# from abc import ABC,abstractmethod
#
# class fruit(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class apple(fruit):
#     def eat(self):
#         print('Apple')
#     def stop(self):
#         print("apple stop")
# class mango(fruit):
#     def eat(self):
#         print('Mango')
#     def stop(self):
#         print('mango stop')
#
# f=fruit()
# a=apple()
# m=mango()
#
# # f.eat()
#
# a.eat()
# m.eat()
#
# a.stop()
# m.stop()

#_------------------------------------------


from abc import ABC,abstractmethod


class A(ABC):
    @abstractmethod
    def show(self):
        pass

class B(A):
    def show(self):
        print('finally I\'m gone')


# o=A()
o1=B()
o1.show()
# o.show()
































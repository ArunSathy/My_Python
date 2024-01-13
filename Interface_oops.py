import abc

class MyInterface(abc.ABC):
    @abc.abstractmethod
    def interface(self):
        pass

class Myclass(MyInterface):
    def interface(self):
        print('calling')

obj=Myclass()
obj.interface()
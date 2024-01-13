class A:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_arun=self.__class__.__name__
        print(class_arun,'Dead')

obj=A()
obj1= obj
obj2=obj1

print(id(obj),id(obj1),id(obj2))
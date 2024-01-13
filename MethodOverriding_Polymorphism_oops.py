# class A:
#     def show(self):
#         print('Show A')
#
# class B(A):
#     def show(self):
#         print('Show B')
#         print('show b 2')
#
# a=B()
# a.show()

#============================================================================

# class parent:
#     parentAttr = 100
#     def __init__(self):
#         print('calling parent constructor')
#     def parentMethod(self):
#         print('calling parent method')
#     def setAttr(self,attr):
#         parent.parentAttr=attr
#     def getAttr(self):
#         print('parent attribute :',parent.parentAttr)
#
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print('calling child constructor')
#     def childMethod(self):
#         print('calling child method')
#     def parentMethod(self):
#         print('overriden parent method') # method overiding
#
# c=child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()

#==============================================================================

# class A:
#     def __init__(self):
#         print('print A')
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('print B')
#     def show(self):
#         print('anandhu')
#
# a=B()
# a.show()

#--------------------------------------------------------


class A:
    def me(self):
        print('Print class A')
class B:
    def me(self):
        print('Print class B')
        

x=B()
x.me()






























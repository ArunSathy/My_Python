# polymorphism ( Poly - many / morphism - forms )
# one thing with different forms
class A:
    def arun(self):
        print('Arun')

class B:
    def arun(self):
        print('Saranya')

def call(name):
    name.arun()

a1=B()

call(a1)

#===========================================================

# it includes 4 different types
# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method Overriding

#======================================================


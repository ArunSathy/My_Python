class student:
    count=0
    def __init__(self,name,mark,age):
        self.name=name
        self.mark=mark
        self.age=age
        student.count+=1
    def display(self):
        print('Name :',self.name,'\nAge  : ',self.age,'\nMark : ',self.mark)
        print('--------------------')
s1=student('arun',68,25)
s1.display()
s2=student('charutty',87,23)
s2.display()
s3=student('athira',45,29)
s3.display()


print("Number of Students : ",student.count)

#------------operation in accesiing attributes----------------

# print(hasattr(s1,'grade')) # check whether it has the mentioned attributes
# print(hasattr(s2,'name'))
#
# print(getattr(s2,'age')) # to get the mention attribute from the details
#
# setattr(s2,'name','saranya') # to set mentioned attribute with new value
# s2.display()
#
# delattr(s3,'standard') # delete a entire object


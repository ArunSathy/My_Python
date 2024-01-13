class student:
    school='Python'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def Average(self):
        return (self.m1+self.m2+self.m3)//3
    def M(self):
        return self.m1

    @classmethod
    def info_school(new):
        return new.school

    @staticmethod
    def info():
        print('End of the Session....!')

x=student(11,12,13)
y=student(15,16,17)

print('Student 1 : ',x.Average())
print('Student 2 : ',y.Average())

print(student.info_school())
student.info()

# Instance method works with Instance variable
# Class method works with Class variable
# Static method works as a stand alone, to do extra
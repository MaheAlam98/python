"""create a student class and takes name and marks of
three subject as arguments as constructor arguments
then create a method to print average"""

# class Student:
#     def __init__(self,name,s1,s2,s3):
#         self.name=name
#         self.s1=s1
#         self.s2=s2
#         self.s3=s3
#     def avg(self):
#         print(f"average:{(self.s1+self.s2+self.s3)/3}")


# s1=Student("tuhin",75,68,39)
# print(s1.avg())


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print(f"average:{sum/len(self.marks)}")


s1=Student("tuhin",[75,68,39,69,20])

print(s1.avg())
class student:
    def __init__(self,name,c):
        print("Student")
        self.name = name
        self.c=c
    
    def info(self):
        print(f"my name is {self.name} and i am in {self.c} student ")

    
a=student("tuhin",'university')
a.info()
b=student("sajid",'xi')
b.info()
        
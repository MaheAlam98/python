class student:
    def __init__(self,name,c):  #constractor
        print("Student")
        self.name = name
        self.c=c
    
    def info(self): #method
        print(f"my name is {self.name} and i am in {self.c} student ")

    
a=student("tuhin",'university')
a.info()
b=student("sajid",'xi')
b.info()
        
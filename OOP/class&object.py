class info:
    name="tuhin"
    semester="3rd year 1st semester"
    district="Bhola"
    def p(self):
        print(f"{self.name} is in now {self.semester} located in {self.district}")

a=info()
a.name="kamal"
a.semester="2rd year 1st semester"
a.district="Barishal"


a.p()
b=info()
b.name="Hasan"
b.semester="2rd year 1st semester"
b.p()


class sdevelopment:
     def __init__(self,name): #constructor automatically call for each object
         
         self.name=name
         
           

d1=sdevelopment("tuhin")
print(d1.name)
class emp:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def details(self):
        print(f"the employee name is {self.name} and id is {self.id}")

class developer(emp):
    def show(self):
        print("Python developer")

a=developer("tuhin",12)

print(a.details())
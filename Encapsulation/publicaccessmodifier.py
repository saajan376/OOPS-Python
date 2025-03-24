class potato:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Age: ",self.age)
m=potato("Saajan",29)
print(dir(m))
print("Name: ",m.name)
m.display()

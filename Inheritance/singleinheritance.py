#single inheritance
class person:
    def __init__(self,name):
        self.name=name
class employee(person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary
emp=employee("John",40000)
print(emp.name, emp.salary)
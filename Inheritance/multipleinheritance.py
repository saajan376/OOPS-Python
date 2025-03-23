class person:
    def __init__(self,name):
        self.name=name
class employee(person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary

class job:
    def __init__(self,salary):
        self.salary=salary

class employeepersonjob(employee,job):
    def __init__(self, name, salary):
        employee.__init__(self,name,salary)
        job.__init__(self,salary)

emp2 = employeepersonjob("Alice", 50000)
print(emp2.name, emp2.salary)
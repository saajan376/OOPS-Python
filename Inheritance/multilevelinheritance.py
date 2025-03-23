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

class manager(employeepersonjob):
    def __init__(self, name, salary,department):
        employeepersonjob.__init__(self,name,salary)
        self.department=department

mgr=manager("Bob",60000,"HR")
print(mgr.name,mgr.salary,mgr.department)
#inheritance using super() method
class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(person):
    def __init__(self, name, idnumber,salary,post):
        super().__init__(name, idnumber)
        self.salary=salary
        self.post=post
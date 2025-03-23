class person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name, self.id)

emp=person("Satyam",102)
emp.display()
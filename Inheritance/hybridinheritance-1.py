'''
Inheritance is a fundamental concept in object-oriented programming (OOP) where a class can inherit attributes and methods from another class. Hybrid inheritance is a combination of more than one type of inheritance. 
'''
class animal:
    def speak(self):
        print("Animal Speaks")
class mammal(animal):
    def give_birth(self):
        print("Mammal gives birth")
class bird(animal):
    def lay_eggs(self):
        print("Bird lays eggs")
class platypus(mammal,bird):
    pass

m=platypus()
m.speak()
m.give_birth()
m.lay_eggs()
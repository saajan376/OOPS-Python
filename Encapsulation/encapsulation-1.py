
#public member
class public:
    def __init__(self):
        self.name="John"
    def displayname(self):
        return self.name
m=public()
print(m.name)

#protected member
class protected:
    def __init__(self):
        self._age=30 #protected attribute

class subclass(protected):
    def displayage(self):
        print(self._age) #This method within the subclass accesses the protected attribute and prints its value. This shows that protected members can be accessed within the class and its subclasses.
m=subclass()
m.displayage()

#private member
class private:
    def __init__(self):
        self.__salary=50000

    def salary(self):
        return self.__salary   
a=private()
print(a.salary)
class protected:
    def __init__(self):
        self._age=30 #protected attribute

class subclass(protected):
    def displayage(self):
        print(self._age) #This method within the subclass accesses the protected attribute and prints its value. This shows that protected members can be accessed within the class and its subclasses.
m=subclass()
m.displayage()
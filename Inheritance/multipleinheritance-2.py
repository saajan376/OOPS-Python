class class1:
    def m(self):
        print("In class 1")
    
class class2(class1):
    def m(self):
        print("In class 2")

class class3(class1):
    def m(self):
        print("In class 3")

class class4(class2,class3):
    pass

obj=class4()
obj.m()

#When you call obj.m() (m on the instance of Class4) the output is In Class2. If Class4 is declared as Class4(Class3, Class2) then the output of obj.m() will be In Class3.
class class1:
    def m(self):
        print("In class 1")

class class2(class1):
    pass

class class3(class1):
    def m(self):
        print("In class 3")

class class4(class2,class3):
    pass

obj=class4()
obj.m()

#this will print in class 3 because class 2 is overridden
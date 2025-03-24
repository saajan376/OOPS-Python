class class1:
    def m(self):
        print("In class 1")

class class2(class1):
    def m(self):
        print("In class 2")
        class1.m(self)

class class3(class1):
    def m(self):
        print("In class 3")
        class1.m(self)

class class4(class2,class3):
    def m(self):
        print("In class 4")
        class2.m(self)
        class3.m(self)

obj=class4()
obj.m()
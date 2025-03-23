class a:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class b(a):
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
d=b()
print(d.feature1())
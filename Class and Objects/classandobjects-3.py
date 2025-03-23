#to define 2 variables we use the __init__method
class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        #this is to initialize the variables inside the function
    def config(self):
        print("Config is",self.cpu,self.ram)

com1=computer("i5",16)
com2=computer("Ryzen 3",8)
com1.config()
com2.config()
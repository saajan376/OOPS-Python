'''
class computer:
    def config(self):
        print("i5,16GB,1TB")
com1=computer()
computer.config(com1)
'''
#one method of calling the function to print without error
#instead of using class name, we can call using the object name

class computer:
    def config(self):
        print("i5,16GB,1TB")
com1=computer()
com1.config()
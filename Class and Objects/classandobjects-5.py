class dog:
    species="canine"
    def __init__(self,name,age):
        self.name=name 
        self.age=age
dog1=dog("buddy",3)
print(dog1.name)
print(dog1.age)
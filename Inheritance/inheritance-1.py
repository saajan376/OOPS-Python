class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class dog(animal):
    def speak(self):
        return f"{self.name} barks!"
d=dog("Cyrus")
print(d.speak())
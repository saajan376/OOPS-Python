class animal:
    def sound(self):
        return "Some nonsense sound"
class dog(animal):
    def sound(self):
        return "Bark"
class cat(animal):
    def sound(self):
        return "Meow"
animals=[dog(),cat(),animal()]
for i in animals:
    print(i.sound())
class vehicle:
    def move(self):
        print("Vehicle moves")
class car(vehicle):
    def drive(self):
        print("Car drives")
class boat(vehicle):
    def sail(self):
        print("Boat sails")
class both(car,boat):
    def bothvehicle(self):
        print("It can both drive as well as sail")
m=both()
m.bothvehicle()
m.move()
m.drive()
m.sail()
#prevent a user from creating an object of that class
# + compels a user to override abstract methds in child class

#abstract class = a class which contains one or more abstract methods
#abstract method = a method that has a declaration but does not have an implementation

from abc import ABC,abstractmethod



class Car(Vehicle):
    def go(self):
        print("You drive the car ")

class Mortorcycle(Vehicle):
    def go(self):
        print("You drive the mortorcycle ")


car = Car()
mortorcycle = Mortorcycle()

vehicle = Vehicle()
vehicle.go()
car.go()
mortorcycle.go()

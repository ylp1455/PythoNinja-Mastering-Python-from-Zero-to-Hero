#prevent a user from creating an object of that class
# + compels a user to override abstract methds in child class

#abstract class = a class which contains one or more abstract methods
#abstract method = a method that has a declaration but does not have an implementation

from abc import ABC,abstractmethod



class Car(Vehicle):
    def go(self):
        print("You drive the car ")

class Mortorcycle(Vehicle):
    import pdb

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car ")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle ")

        def stop(self):
         print("You stop the motorcycle ")

# Instantiate objects
car = Car()
motorcycle = Motorcycle()

# This will raise an error because we cannot instantiate an abstract class
vehicle = Vehicle()

# Debugging
pdb.set_trace()

# Call methods on objects
car.go()
motorcycle.go()


car = Car()
mortorcycle = Mortorcycle()

#vehicle = Vehicle()
#vehicle.go()
#car.go()
#mortorcycle.go()

car = Car()
car.go()
mortorcycle = Mortorcycle()

car.stop()
mortorcycle.stop()
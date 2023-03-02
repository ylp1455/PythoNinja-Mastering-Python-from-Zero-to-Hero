#Method chaining  = calling multiple methods sequentially each call perform an action on the same object and return self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You stop the engine")
        return self

        
car = Car()
#car.turn_on().drive()
# by using method chaining you can activate 2 or more methods sequentially without writting multiple line of codes

#car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

#if you want to chain mny methods add back slashes like this so it'll be easy to read afterwards
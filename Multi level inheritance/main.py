#when a derived class inherits another derived class from another challange

class Organisms:
    alive = True

class Animals(Organisms):
    def eat(self):
        print ("This animal is eating")

class dog(Animals):

    
      def bark(self):
       print ("This dog is barking")


dog = dog()
print(dog.alive)
dog.eat()
dog.bark()
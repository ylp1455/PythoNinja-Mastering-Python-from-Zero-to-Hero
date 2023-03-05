#Duck typing = concept where the class of an object is less important than the methods of the object.class type is not checkd if minimum methods/attributes are present "If it walks like a duck , and it quaks like a duck, it is a duck, them it must be a duck"

class Duck:

    def walk (self):
        print("This duck is walking")
    
    def talk (self):
        print("This duck is quwaking")

class Chicken:
    def walk (self):
        print("This chicken is walking")
    
    def talk (self):
        print("This chicken is clucking")

class Person():
    def catch (self , duck):
        duck.walk
        duck.talkuck.talk
        print("You caught an critter")
              
duck = Duck()
Chicken = Chicken()
person = Person()

person.catch(duck)
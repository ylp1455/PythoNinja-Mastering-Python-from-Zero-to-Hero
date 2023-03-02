class Animals:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animals):
    
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()
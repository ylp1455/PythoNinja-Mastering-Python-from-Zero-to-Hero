#clases can have children.
#Childern clasess will inherit from parent class.
#childern classcan implement ther own and unqiue methods.


class animal:
    alive = True
    def eat(self):
        print ("This animal is eating")

    def slumber(self):
         print ("This animal is sleeping")

class Rabbit(animal):
    def run(self):
        print ("This rabbit is running")

class Fish(animal):
    def swim(self):
        print ("This fish is swiming")
class Hawk(animal):
    def fly(self):
        print ("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)

fish.eat()
hawk.fly()


rabbit.run()
fish.swim()
hawk.fly()
#multiple instances = When a child class is derived from more than one parent class

class prey:
    def flee():
        print("This animals flees")

class predator:
    def hunts():
        print("This animals hunts")

class rabbit(prey):
    pass

class hawk(predator):
    pass
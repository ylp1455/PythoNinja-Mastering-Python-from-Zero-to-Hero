class prey:
    def flee(self):
        print("This animal flees")

class predator:
    def hunts(self):
        print("This animal hunts")

class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(predator,prey):
    pass


rabbit = rabbit()
hawk = hawk()
fish = fish()

rabbit.flee()
hawk.hunts()
fish.flee()
fish.hunts()
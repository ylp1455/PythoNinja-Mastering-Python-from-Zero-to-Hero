#Walrus operatr :=

#new to python 3.8
#assinment expression aka walrus operator
#assign value to variable as part of a larger  expression

happy = True
print(happy)

print(happy := True)




#foods = list()
#while True:
#   food = input("What food would you like to eat? ")
#    if food == "quit":
#        break
#   foods.append(food)

#we can write the same program using wallrus operator using less code than above code.

foods = list()
while food := input("What food would you like to eat? ") != "quit":
    foods.append(food)


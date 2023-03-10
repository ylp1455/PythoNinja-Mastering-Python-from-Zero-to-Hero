#lambda functions = function written in 1 line using lambda keyword accepts any number of arguments.But only has one expression.
#Think of it as a shortcut
#(usefull if needed for short period of time, throw-away )

#lambda parameters:expression


# def double(x):
#     return x*2

#print(double(5))

# double = lambda x:x*2

# print(double(5))

# double = lambda x:x*2
# multiply = lambda x,y : x*y
# add = lambda x,y,z : x+y+z

# print(add(5,6,7)



ful_name = lambda first_name , last_name : first_name + " " + last_name
print(ful_name("yasiru","Perera"))

age_check = lambda age : True if age >= 18 else False
print(age_check(18))
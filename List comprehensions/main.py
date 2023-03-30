# list comprehenison = a way to create new list with less Syntax
#                     can mimic certain lambda functions,,easier to read
#                     list = [expression (if/else) for item  in iterable]


# squares = []                 # Creates an empty list
# for i in range(1,11):        # Creates a for loop
#     squares.append(i*i)      # Define what each loop iteration should do 
# print(squares)

# squares = [i * i for i in range(1,11)]
# print(squares)


students = [100,90,80,70,60,50,40,30,0]

# passed_students = list (filter(lambda x: x >= 60 ,students))

# passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "Failed" for i in students]

print(passed_students)
# list comprehenison = a way to create new list with less Syntax
#                     can mimic certain lambda functions,,easier to read
#                     list = [expression for item  in iterable]


squares = []                 # Creates an empty list
for i in range(1,11):        # Creates a for loop
    squares.append(i*i)      # Define what each loop iteration should do 
print(squares)



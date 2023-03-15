# filter() = create a collection of element for which a funtion returns an

# filter(function, iterable)

freiends = [("Rachel" , 19),
            ("Monica",18),
            ("Phoebe" , 17),
            ("Joey",16),
            ("chandler" , 21), 
            ("Ross",20) 
           ]
age = lambda data:data[1] >=18
drinking_buddies = list(filter(age,freiends))

for i in drinking_buddies:
    print(i)
# Dictionary comprehension = create dictionary using an expresion
#                            can replace for loops and certain lambda functions
        
# dictionary  = {key : expression for (key,value) in iterable}


# Define a dictionary with temperature values in Fahrenheit for different cities
cities_in_F = {'New York' : 32, 'Boston' : 75, "Los Angeles" :100, 'Chicago' :50}

# Create a new dictionary with the same keys as `cities_in_F`, but with Celsius values instead of Fahrenheit
# The expression used to calculate the Celsius values is incorrect, it should be: (value - 32) * (5/9)
cities_in_c = {key: round((value - 32) * (5/9)) for (key,value) in cities_in_F.items()}

# Print the new dictionary
# print(cities_in_c)

# -----------------------------------------------------------------------------------------------------------

# dictionary  = {key : expression for (key,value) in iterable if condition}

weather = {'New York' : "snowing" , 'Boston' : "Sunny" , 'Los Angeles' : "Sunny" , 'Chicago' : "Cloudy"}


sunny_weather = {key : value for (key,value) in  weather.items() if value  == "Sunny"  }

# print(sunny_weather)


# --------------------------------------------------------------------------------
# dictionary  = {key : (if/else) for (key,value) in iterable}


cities = {'New York' : 32, 'Boston' : 75, "Los Angeles" :100, 'Chicago' :50}


desc_cities = {key : (" Warm " if value >=40 else "Cold") for (key,value) in cities.items()}

#print(desc_cities)


#----------------------------------------------------------------------------------------
# dictionary  = {key : function(value) for (key,value) in iterable}

def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >= 40:
        return "Warm"
    else:
        return "cold"
    

cities = {'New York' : 32, 'Boston' : 75, "Los Angeles" :100, 'Chicago' :50}


desc_cities = {key : check_temp(value) for (key,value) in cities.items()}


print(desc_cities)
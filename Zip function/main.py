# zip(*iterables) = aggregate elements from two or more iterables(list,tuple,sets,etc.)
#                   create a zip object with paried elements stored in tuples for each element


usernames = ["Dude" , "John" , "wick"]
password = ("p@ssword" , "abc123" , "guest")


# user = list(zip(usernames,password))


user = dict(zip(usernames,password))
print(type(user))
      

# for i in user:
#     print (i)

for key , value in user.items():
    print(key + " : " + value)
# zip(*iterables) = aggregate elements from two or more iterables(list,tuple,sets,etc.)
#                   create a zip object with paried elements stored in tuples for each element


usernames = ["Dude" , "John" , "wick"]
password = ("p@ssword" , "abc123" , "guest")
login_date = ["26/01/2001" , "4/11/2000" , "15/08/200"]


# user = list(zip(usernames,password))


user = zip(usernames,password,login_date)
print(type(user))
      

for i in user:
    print(i)
  
# for key , value in user.items():
#     print(key + " : " + value)
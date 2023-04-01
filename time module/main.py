import time

# print(time.ctime(10000))
#convert a time expressed in seconds since epoch to a readable string
# epoch = when your computer thinks time began

# print(time.time()) #return curent seconds since epoch


# print(time.ctime(time.time()))

# time_object = time.localtime()

# print(time_object)

# local_time = time.strftime("%d %B %Y       %H : %M : %S ",time_object)
# print(local_time) 


# utc_time = time.gmtime()

# print(utc_time)


# -------------------------------------------------------------------------------------------
# local_time = "1 April ,2020"
# time_obj = time.strptime(local_time, "%d- %B -%Y" )
# print(time_obj)
 

#  ----------------------------------------------------------------------------------------
# (year, month, day, hour, minute, second ,#day of the week , # day of the year ,dst)

time_tuple = (2020, 4, 1, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)

time_string = time.mktime(time_tuple)

print(time_string)




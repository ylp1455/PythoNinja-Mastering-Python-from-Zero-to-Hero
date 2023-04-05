#daemon thread = a thread that runs in the background,not important for program to run
# daemon         your program will not wait for dameon threads to complete before exiting
#                non daemon threads cannot be killed,stay alive until ists complete
#  ex:-background tasks,garbage collection,waiting for input



import threading
import time


def timer():
    print()
    count = 0
    while true:
        time.sleep(1)
        count = count + 1
        print("logged in for : " , count , "seconds")



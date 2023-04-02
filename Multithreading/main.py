# Thread  = a flowof execution.like seperate order of instructions
#           however each thread takes a turn running to achieve concurency,
#           GIL = (Global Interreter Lock)
#           allows only one thread to hold the control of the python interpreter.



# cpu bound = program/task spends most of its time waiting for internal events


# io bound = program/task spends most of its time waiting forexternal events


import threading
import time

def eat_brakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You had coffe")

def study():
    time.sleep(5)
    print("You finished study")


x = threading.Thread(target= eat_brakfast,args=())
x.start()

y = threading.Thread(target=drink_coffee,args=())
y.start()

z = threading.Thread(target=study,args=())
z.start()


x.join()
y.join()
z.join()


# eat_brakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
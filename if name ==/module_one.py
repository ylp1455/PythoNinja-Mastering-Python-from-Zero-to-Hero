# *************************************************************

#     if __name__ == '__main__'

# *************************************************************
# why:
#     1. Module can be run as standalone program
#     2. Module can be imported and used by other modules.




# python interpreter sets "special variables" , one of which os __name
# python will assign the __name__ variable a value of '__main__' if its the initial module being run

# import module_two
# print(__name__)

# print(module_two.__name__)


# if __name__ == '__main__':
#     print("Running this module directly")

# else :
#     print ("Running other module indirectly")
    


def hello ():
    print("Hello world")


if __name__ == '__main__':
    hello ()

else :
    print ("Running other module indirectly")
    

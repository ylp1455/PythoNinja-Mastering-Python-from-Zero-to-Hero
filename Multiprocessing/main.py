# python multiprocessing


# multiprocessing = running task in parerel on diffrent cpu cores,bypass GIL used for therer
#                   multiprocessing = better for cpu bound tasks(heavy cpu usage)
#                   multithredding = better for io bound tasks (waiting around)


from multiprocessing import Process , cpu_count
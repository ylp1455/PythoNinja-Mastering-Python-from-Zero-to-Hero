# python multiprocessing


# multiprocessing = running task in parerel on diffrent cpu cores,bypass GIL used for therer
#                   multiprocessing = better for cpu bound tasks(heavy cpu usage)
#                   multithredding = better for io bound tasks (waiting around)


from multiprocessing import Process, cpu_count
import time 

def count(num):
    count = 0
    while count < num:
        count += 1

def main():
    start_time = time.perf_counter()
    print(cpu_count())

    a = Process(target=count, args=(12500000,))
    b = Process(target=count, args=(12500000,))
    c = Process(target=count, args=(12500000,))
    d = Process(target=count, args=(12500000,))
    e = Process(target=count, args=(12500000,))
    f = Process(target=count, args=(12500000,))
    g = Process(target=count, args=(12500000,))
    h = Process(target=count, args=(12500000,))

    a.start() # start the process
    b.start() 
    c.start() 
    d.start()
    e.start() 
    f.start() 
    g.start()  
    h.start()

    a.join() # wait for the process to finish
    b.join()
    c.join()
    d.join()
    e.join() 
    f.join()
    g.join()
    h.join()

    end_time = time.perf_counter()
    print("finished in : " , end_time - start_time , "seconds")

if __name__ == "__main__":
    main() 

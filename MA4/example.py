from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp 
import concurrent.futures as future

def runner(n):
    print(f"Performing a costly function {n}")
    pause(n)
    return f"Function {n} has completed"

def main():
    start = pc()

    p = [5, 4, 3, 2, 1]
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(runner)
        #p1 = ex.submit(runner, 2)#some_arg, some_other_arg, ...) # Starts first process,→
        #p2 = ex.submit(runner, 1)#some_arg, some_other_arg, ...) # Starts second process,→
        #r1 = p1.result() # Program waits until p1 is complete before assigning r2
        #r2 = p2.result()
        #print("all done") # Will be printed once all processes are completed
    for r in results:
        print(r)
    
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")


def blah2():
    start = pc()
    processes = []
    for _ in range(10):
        p = mp.Process(target=runner) #, args=None)
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")


def blah():
    start = pc()
    #for i in range(10):
    #    runner()
    p1 = mp.Process(target=runner)
    p2 = mp.Process(target=runner)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

if __name__ == "__main__":
    main()
    
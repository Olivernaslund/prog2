"""
Student: Oliver Näslund
Mail: oliver.naslund@gmail.com
Reviewed by: Hannah M
Date reviewed: 16 Maj 2023
"""


import matplotlib.pyplot as plt
import random
from time import perf_counter as pc
from time import sleep as pause
from math import pi, gamma
import functools
import concurrent.futures as future


def pi_calc(n, plot=False):
    punkter_in_x = [] ; punkter_in_y = []
    punkter_ut_x = [] ; punkter_ut_y = []
    for i in range(n):
        x = random.uniform(-1, 1) ; y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            punkter_in_x.append(x) ; punkter_in_y.append(y)
        elif x**2 + y**2 > 1:
            punkter_ut_x.append(x) ; punkter_ut_y.append(y)
    pie = 4*len(punkter_in_x)/n
    if plot:
        plt.plot(punkter_in_x, punkter_in_y, 'ro', markersize = 4)
        plt.plot(punkter_ut_x, punkter_ut_y, 'bo', markersize = 4)
        plt.show()
    return pie

def hypersphere(n, d, r=1):
    start = pc()
    vec_längder_in = list(filter(lambda x: x < 1, [functools.reduce(lambda x,y: x+y, map(lambda x: x**2, [random.uniform(0,1) for i in range(d)])) for e in range(n)])) 
    end = pc()
    return (2**d)*len(vec_längder_in)/n, f'time: {round(end-start, 2)}'


def hypersphere_time(n, d, r=1, processes=10):
    start = pc()

    with future.ProcessPoolExecutor() as ex:
        #results = []
        #for _ in range(processes):
        #    results.append(ex.submit(hypersphere, int(n/processes), d, r)) #använd map
        results = ex.map(hypersphere, [int(n/processes) for i in range(processes)], [d for i in range(processes)])
        #results = [i.result() for i in results]
        results = [i[0] for i in results]
                

    end = pc()
   # print(f"Process took {round(end-start, 2)} seconds")
    return sum(results)/processes, f'time: {round(end-start, 2)}'


def hypersphere_exact(n, d, r=1):
    return (pi**(d/2)/(gamma(d/2 + 1)))*r**2

    
def main():
    print('----Calculation of pi with graphs (MA4:1.1)----')
    for i in [1000, 10000, 100000]:
        print(f'pi = {pi_calc(i, True)} for n = {i}')

    print('----Calculation hypersphere (MA4:1.2)----')
    print('Calculation (n,d) = (100000, 2)', hypersphere(100000, 2))
    print('Exact Calculation (n,d) = (100000, 2)', hypersphere_exact(100000, 2))
    print('Calculation (n,d) = (100000, 11)', hypersphere(100000,11))
    print('Exact Calculation (n,d) = (100000, 11)', hypersphere_exact(100000,11))

    print('----Multiprocessing calculation hypersphere (MA4:1.3)----')
    n = 1000000 ; d = 11
    print('Calculation hypersphere without multiprocessing: ', hypersphere(n,d)) #ca 29sec
    print('Exact calculation hypersphere: ',hypersphere_exact(n, d))
    print('Calculation hyperesphere with multiprocessing: ',hypersphere_time(n, d, 1, 10)) #ca 15 sec
    
    print('Done')

    

if __name__ == "__main__":
    main()


    

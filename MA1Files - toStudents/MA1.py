
"""
Solutions to module 1
Student: Oliver Näslund
Mail: oliver.naslund@gmail.com
Reviewed by: Axel Wohlin 
Reviewed date: 23/03 - 2023
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib functionen.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def power(x, n: int):                        # Optional
    """ Computes x**n using multiplications and/or division """
    if n == 0:
        return 1
    elif n > 0:
        return x*power(x,n-1)
    elif n < 0:
        return 1/x*power(x,n+1)

def multiply(m: int, n: int) -> int:         # Compulsory
    """ Computes m*n using additions"""
    if n > 0:
        return m + multiply(m, n-1)
    else:
        return 0


def divide(t: int, n: int) -> int:           # Optional
    """ Computes m*n using subtractions"""
    if t == n:
        return 1
    elif t > n:
        return 1 + divide(t-n,n)
    else:
        return 0


def harmonic(n: int) -> str:                 # Compulsory
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n > 1:
        return 1/n + harmonic(n-1)
    elif n == 1:
        return 1



def digit_sum(x: int) -> int:                # Optional
    """ Computes and returns the sum of the decimal digts in x"""
    if x == 0:
        return 0
    elif x > 0:
        return x % 10 + digit_sum(int(x/10))

def get_binary(x: int) -> str:               # Compulsary
    """ Returns the binary representation of x """
    if x == 0:
        return f'0'
    if x == 1:
        return f'1'
    elif x > 0:
        return get_binary(int(x/2)) + f'{x % 2}' 
    elif x < 0:
        return f'-' + get_binary(abs(x))


def reverse_string(s: str) -> str:           # Optional
    """ Returns the s reversed """
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[-1:]) + reverse_string(s[:-1])


def largest(a: iter):                        # Compulsory
    """ Returns the largest element in a"""
    if len(a) <= 1:
        return a[0]
    if a[0] > a[-1]:
        return largest(a[:-1])
    if a[0] < a[-1]:
        return largest(a[1:])


def count(x, s: list) -> int:                # Compulsory
    """ Counts the number of occurences of x on all levels in s"""
    if len(s) == 0:
        return 0
    elif s[0] == x:
        return 1 + count(x, s[1:])
    elif type(s[0]) == list:
        return count(x, s[0]) + count(x,s[1:])
    else:
        return count(x,s[1:])


def zippa(l1: list, l2: list) -> list:       # Compulsory
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if len(l1) <= 0 or len(l2) <= 0:
        return l1 + l2
    else:
        return [l1[0]] + [l2[0]] + zippa(l1[1:], l2[1:])


def bricklek(f: str, t: str, h: str, n: int) -> str:  # Compulsory
    """ Returns a string of instruction ow to move the tiles """
    if n == 0: 
        return []
    if n == 1: 
        return [f'{f}->{t}']
    else:
        return bricklek(f, h, t, n-1) + bricklek(f, t, h, 1) + bricklek(h, t, f, n-1)



def fib(n: int) -> int:                       # Compulsory
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    prev = {0:0, 1:1}
    def _fib2(n):
        if n not in prev:
            prev[n] = _fib2(n-1) + _fib2(n-2)
        return prev[n]
    return _fib2(n)


def main():
    print('\nCode that demonstates my implementations\n')
    
    res = bricklek('f','t','h', 2)
    print(res)
    print(len(res))

    print(f'Tid för 50 brickor {(2**50 - 1)/(60*60*24*365.25)} år')


    print('\n\nCode for analysing fib\n')


    c_list = []
    for i in range(10,30,1):
        start_t = time.perf_counter()
        fib(i)
        stop_t2 = time.perf_counter() - start_t
        c_list.append(stop_t2/1.618**i)
    
    #print(c_list)

    # t_n = c * f_n ; f_n = theta(..)
    # start 
    n0 = 10
    start_t = time.perf_counter()
    fib(n0)
    stop_t = time.perf_counter() - start_t
    t_n1 = stop_t 

    for n in range(n0,30,1):
        start_t = time.perf_counter()
        fib(n)
        stop_t2 = time.perf_counter() - start_t
        t_n2 = stop_t2 ; f_n1 = 1.618**n

        print(f'''
        *** n = {n} ***
        Uppmätt tid = {t_n2}
        Beräknad tid = {t_n1*1.618**(n-n0)}
        ''')

    n=30
    start_t = time.perf_counter()
    fib(n)
    stop_t = time.perf_counter() - start_t

    t_n1 = stop_t ; f_n1 = 1.618**n
    c = t_n1 / f_n1
    f_n = 1.618**n
    t_n = c*f_n

    print(f'Uppmätt tid = {t_n1}')
    print(f'Beräknad tid = {t_n}')

    print(c)

    #fib(50)
    t_50 = c*1.618**(50)
    print(f'N = 50; {t_50/(60)} minuter') 

    #fib(100)
    t_100 = c*1.618**(100)
    print(f'N = 100; {t_100/(60*60*24*365.25)} år') 



    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  Antalet förflyttningar som kravs för N antal brickor är 2^N - 1, vilket innebär antalet förflyttningar för 50 brickor är 2^50 - 1 sekunder
  Vilket motsvarar 35.7 miljoner år
  
  
  
  Exercise 17: Time for Fibonacci:
  
  För N = 50 skulle det ta ca 76.5 minuter
  För N = 100 hade det tagit ca 4.1 miljoner år
  
  
  Exercise 20: Comparison sorting methods:
  
  t_n = c * f_n <=> c = t_n / f_n
  insticksortering, theta(n**2) f1
  mergesort, theta(n*log(n))  f2
  
  t_1000 = c1 * f1_1000 = c2 * f2_1000 = 1 s
  c1 = 1 / 1000^2 = 1/10^6
  c2 = 1 / 1000*log(1000) = 1 / 3*10^3

  n = 10^6
  För instrickssortering: t_n = c1 * n^2 = 1/10^6 * 10^12 = 10^6 s = 11.57 dagar
  För mergesort: t_n = c2 * n*log(n) = 1/3*10^3 * 10^6 * log(10^6) = 1 / 3*10^3 * 10^6 * 6*log(10) = 2*10^3 s = 33 minuter

  n = 10^9
  För instricksosrting: t_n = c1 * n^2 = 1/10^6 * 10^18 = 10^12 s = 31.7 tusen år
  För mergesort: t_n = c2 * n*log(n) = 1/3*10^3 * 10^9 * log(10^9) = 1/3*10^3 * 10^9 * 9*log(10) = 3*10^6 s = 34.7 dagar 
  

  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  A: n på n sek ; A_t_n = n
  B: c*n*log(n) sekunder ; B_t_n = c*n*log(n)

  För B, n=10 B_t_n = 1 
  c = 1 / n*log(n) = 1 / 10*log(10) = 1 / 10

  När gäller att A_t_n < B_t_n:
  n < 0.1*n*log(n) => 1 < 0.1*log(n) => 10 < log(n) => 10^10 < n

  När n är större än 10^10 så är tar A kortare tid
  
  
  
  
  
  





"""

"""
Solutions to module 2 - A calculator
Student: Oliver Näslund
Mail: oliver.naslund@gmail.com
Reviewed by: Kalle Bylander Camitz
Reviewed date: 19 Apri 2023
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""


from MA2tokenizer import TokenizeWrapper
import math
from tokenize import TokenError

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

     
def fib(n, cache={1: 1, 2: 1}):
    if n % 1 != 0 or n < 0:
        raise EvaluationError(f"Argument to fib is {n}. Must be integer >= 0")
    if n in cache:
        return int(cache[n])
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return int(cache[n]) 

def mean(list):
    return sum(list)/len(list)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if wtok.is_at_end() == False:
        raise SyntaxError("Not at end")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name(): # and wtok.has_next() == False:
            variables[wtok.get_current()] = result
            wtok.next()
            if wtok.get_current() != '=' and wtok.get_current() != ')' and wtok.is_at_end() == False:
                    raise SyntaxError("Expected variable after '='")
        elif expression(wtok, variables) != result:
            raise SyntaxError("Equation not balanced")

    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        wtok.next()
        if wtok.get_previous() == '+':
            result = result + term(wtok, variables)
        elif wtok.get_previous() == '-':
            result = result - term(wtok, variables)
    return result
    


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        wtok.next()
        if wtok.get_previous() == '*':
            result = result * factor(wtok, variables)
        elif wtok.get_previous() == '/':
            try:
                result = result/factor(wtok, variables)
            except ZeroDivisionError as ze:
                raise EvaluationError("Division by zero")
           
    return result


def factor(wtok, variables):
    """ See syntax chart for factor
        Follow the syntax chart as closely as possible!
        Check only for syntax error error - not for evaluation errors!
    """
    FUNCTIONS_1 = {'sin':math.sin, 'cos':math.cos, 'log':math.log, 'exp':math.exp, 'fib':fib, 'fac':math.factorial, 'abs':abs}
    FUNCTIONS_N = {'sum': sum, 'max': max, 'min': min, 'mean': mean}

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    
    elif wtok.get_current() in FUNCTIONS_1:
        funktion = FUNCTIONS_1[wtok.get_current()]
        wtok.next()
        if wtok.get_current() != '(':
            raise SyntaxError("Expected '('")
        else: 
            wtok.next()
            try:
                result = funktion(assignment(wtok, variables))
            except ValueError as ve:
                raise EvaluationError(f"{ve}")
            if wtok.get_current() != ')':
                raise SyntaxError("Expected ')'")
            else:
                wtok.next()

    
    elif wtok.get_current() in FUNCTIONS_N:
        funktion = FUNCTIONS_N[wtok.get_current()]
        wtok.next()
        list = arglist(wtok,variables)
        try:
            result = funktion(list)
        except ValueError as ve:
            raise EvaluationError(f'{ve}')

       # if len(list) != 0:
       #     result = funktion(list)
       # else:
       #     raise EvaluationError(f"Nothing in {wtok.get_previous()} to evaluate")

    elif wtok.is_name():
        wtok.next()
        if wtok.get_previous() not in variables:
            raise EvaluationError("Variable not defined")
        else:
            result = float(variables[wtok.get_previous()])
        
    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)

    elif wtok.get_current() == '+':
        wtok.next()
        result = factor(wtok, variables)


    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
     #   if wtok.is_number():
     #       raise SyntaxError("Expected operator after number")

    elif wtok.is_at_end():
        result = wtok.get_current()

    else:
        raise SyntaxError(
            "Expected number or '('")
            
    return result



def arglist(wtok,variables):
    arglist = []

    if wtok.get_current() == '(':
        wtok.next()
        arglist.append(assignment(wtok, variables))
        while wtok.get_current() == ',':
            wtok.next()
            arglist.append(assignment(wtok, variables))
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
    
    else:
        raise SyntaxError("Expected '(' ")

    return arglist

def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file.
    
    You need to add handling of EvaluationError in this function!
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    init_file = 'MA2init.txt'
    lines_from_file = ''

    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'vars':
            for i in variables:
                print(i, f'= {variables[i]}')

        elif wtok.get_current() == 'quit':
            print('Bye')
            exit()
        
        

        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvaluationError as ee:
                print("***Evaluation error: ", ee)

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')


if __name__ == "__main__":
    main()



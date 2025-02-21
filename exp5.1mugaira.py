# Aim: Write a Program to with calculator handle Exception 
# Branch: COMPS
# Year: 2nd
# Sem: 4
# Subject:Python lab
# Name: Pathan Mugaira Zakeer
# UIN:231P084
# Roll No.:25

class FormulaError(Exception):
    pass


def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        if n2 == 0:
            raise FormulaError('cannot divide by zero')
        return n1 / n2
    if op == '%':
        if n2 == 0:
            raise FormulaError('cannot mod by zero')
        return n1 % n2
    raise FormulaError(f'Invalid operator {op}')

def parse_input(user_input):
    input_list = user_input.split()
    if len(input_list) != 3:
        raise FormulaError('Input does not consist of three elements')
    n1, op, n2 = input_list
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        raise FormulaError('The first and third input value must be numbers')
    return n1, op, n2

while True:
    user_input = input('>>> ')
    if user_input == "QUIT":
        break
    
    n1, op, n2 = parse_input(user_input)
    result = calculate(n1, op, n2)
    print(result)
   

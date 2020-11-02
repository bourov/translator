# put your python code here

n1 = float(input())
n2 = float(input())
op = input()

steps = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b,
    'mod': lambda a, b: a % b,
    'pow': lambda a, b: a ** b,
    'div': lambda a, b: a // b
}

try:
    print(steps[op](n1, n2))
except ZeroDivisionError:
    print('Division by 0!')


eval('2+2')

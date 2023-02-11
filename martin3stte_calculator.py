
# Calculator by Martin3stte. All Rights Reserved.

def sum(a, b):
    return (a + b)

a = int(input('Sum. Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

def sub(c, d):
    return (c - d)

c = int(input('Substraction. Enter 1st number: '))
d = int(input('Enter 2nd number: '))

print(f'Substraction of {c} and {d} is {sub(c, d)}')

def multiplication(e, f):
    return (e * f)

e = int(input('Multiplication. Enter 1st number: '))
f = int(input('Enter 2nd number: '))

print(f'Multiplication of {e} and {f} is {multiplication(e, f)}')

def div(g, h):
    return (g / h)

g = int(input('Division. Enter 1st number: '))
h = int(input('Enter 2nd number: '))

print(f'Division of {g} and {h} is {div(g, h)}')


print("Thanks for using Martin3stte's calculator.")

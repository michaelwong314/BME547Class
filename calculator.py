# calculator.py

def add(x, y):
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return z

def subtract(x, y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))
    return z
    
def multiply(x, y):
    z = x * y
    print("{} * {} = {}".format(x, y, z))
    return z
    
x = input("Enter a letter: ")
print("You entered {}".format(x))
if x == "a":
    d = add(56, 73)
    if d > 100:
        print("This number is too high.")
if x == "b":
    d = subtract(20, 3)
if x == "c":
    d = multiply(4, 10)
elif x == "s":
    a = 20
    b = -3
    c = a - b
    print("{} + {} = {}".format(a, b, c))
elif x == "m":
    a = 3
    b = -4
    c = a * b
    print("{} * {} = {}".format(a, b, c))
else:
    print("The {} command is not recognized.".format(x))
print("Done")

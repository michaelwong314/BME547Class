# calculator.py

def add(num1, num2):
    z = num1 + num2
    print("{} + {} = {}".format(num1, num2, z))
    symbol = "+"
    return z, symbol

def subtract(num1, num2):
    z = num1 - num2
    print("{} - {} = {}".format(num1, num2, z))
    return z
    
def multiply(num1, num2):
    z = num1 * num2
    print("{} * {} = {}".format(num1, num2, z))
    return z
    
def divide(num1, num2):
    z = num1 / num2
    print("{} / {} = {}".format(num1, num2, z))
    return z

x = input("Enter a letter: ")
print("You entered {}".format(x))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#print("You entered {} and {}".format(x))

if x == "a":
    d = add(num1, num2)
elif x == "s":
    d = subtract(num1, num2)
elif x == "m":
    d = multiply(num1, num2)
elif x == "d":
    d = divide (num1, num2)
    
#elif x == "j":
#    a = 20
#    b = -3
#    c = a - b
#    print("{} + {} = {}".format(a, b, c))
#elif x == "k":
#    a = 3
#    b = -4
#    c = a * b
#    print("{} * {} = {}".format(a, b, c))
else:
    print("The {} command is not recognized.".format(x))

print("Done")

# input letter
# input two numbers
# use to call
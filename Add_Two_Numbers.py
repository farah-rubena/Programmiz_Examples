#Python Program to Add Two Numbers
def add_num(x,y):

    return x + y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
summation = add_num(x,y)
print(f"Sum of {x} and {y} is: {summation} ")
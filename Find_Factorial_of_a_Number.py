# Python Program to Find the Factorial of a Number
# The factorial of a number is the product of all the integers from 1 to that number.

def find_factorial(num):

    factorial = 1
    for _ in range(1, num+1):
        factorial *= _

    return factorial


n = int(input("Enter a number: "))
fact = find_factorial(n)
print(fact)

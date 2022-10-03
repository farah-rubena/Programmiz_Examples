# Python Program to Print the Fibonacci sequence up to the n-th term
# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.

def find_fibonnaci(nth_value):

    n1, n2 = 0, 1
    count = 0

    if value == 0:
        return "Enter a positive integer"
    while count < value:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


value = int(input("Enter the nth-value: "))
fibonnaci = find_fibonnaci(value)
print(fibonnaci)

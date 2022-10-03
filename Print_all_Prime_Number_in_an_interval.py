# Python Program to Print all Prime Numbers in an Interval


def print_primes(lower, upper):

    for num in range(lower, upper+1):
        if num > 1:
            for _ in range(2, num):
                if num % _ == 0:
                    break
            else:
                print(num)


lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

primes = print_primes(lower, upper)
print(primes)

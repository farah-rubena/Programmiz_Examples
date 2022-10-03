# Python Program to Check if a Number is Odd or Even


def even_odd(num):

    if num % 2 == 0:
        return "Even"
    return "Odd"


n = int(input("Enter a number: "))
eve_odd_checker = even_odd(n)
print(f"The number {n} is {eve_odd_checker}")

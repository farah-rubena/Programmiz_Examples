# Python Program to Check Prime Number


def check_prime(num):

    if num <= 1:
        return "Not Prime"

    for _ in range(2, num):
        if num % _ == 0:
            return "Not Prime"
    else:
        return "Prime"


n = int(input("Enter a number: "))
prime_check = check_prime(n)
print(f"{n} is {prime_check}")

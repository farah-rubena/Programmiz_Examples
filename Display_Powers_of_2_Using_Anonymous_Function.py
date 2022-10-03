# Python Program to Display Powers of 2 Using Anonymous Function


def power_of_two(num):

    for _ in range(10):
        print(f"{num} raised to the power of {_} is {num**_}")


n = int(input("Enter a number: "))
power_of = power_of_two(n)
print(power_of)

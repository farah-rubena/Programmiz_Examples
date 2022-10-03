# Python Program to Find the Sum of Natural Numbers


def sum_natural_num(num):

    sum = 0

    for _ in range(num+1):
        sum += _
    return sum


n = int(input("Enter a number: "))
natural_sum = sum_natural_num(n)
print(f"The sum of all natural numbers leading upto {n} is {natural_sum}")

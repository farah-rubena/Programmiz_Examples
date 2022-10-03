# Python Program to Display the multiplication Table


def display_multiplication(num):

    count = 0
    for _ in range(1, 11):
        count += 1
        print(f"{num} * {count} = {num * count}")


x = int(input("Enter the number : "))
multiplication_table = display_multiplication(x)
print(multiplication_table)

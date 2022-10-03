# Python Program to Find the Largest Among Three Numbers


def largest_among_three(x, y, z):

    if x > y and y > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))
largest = largest_among_three(x, y, z)
print(f"The largest number is {largest}")

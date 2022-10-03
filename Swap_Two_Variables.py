# Python Program to Swap Two Variables


from re import A


def swap_variables(x, y):

    a = 0
    a = x
    x = y
    y = a

    return x, y


x = input("Enter the value for 'x': ")
y = input("Enter the value for 'y': ")
swapped = swap_variables(x, y)
print(f"The new value of 'x' and 'y' is {swapped}")

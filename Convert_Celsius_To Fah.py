# Python Program to Convert Celsius To Fahrenheit


def celsuis_to_fah(cel):

    return (cel * 1.8) + 32


cel = float(input("Enter the celsius to be converted to fahrenheit: "))
converted_fah = celsuis_to_fah(cel)
print(converted_fah)

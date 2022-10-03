# Python Program to Check if a Number is Positive, Negative or 0


def positive_negative_checker(num):

    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return 0


num = int(input("Enter a number: "))
checker = positive_negative_checker(num)
print(f"The number is {checker}")

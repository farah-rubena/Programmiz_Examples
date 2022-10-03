# Python Program to Check Leap Year


def check_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap"
            else:
                return "Not Leap"
        else:
            return "Leap"
    else:
        return "Not Leap"


y = int(input("Enter the year: "))
leap_checker = check_leap(y)
print(f"The year {y} is {leap_checker}")

# Python Program to Find Numbers Divisible by Another Number


def divisible(num):

    my_list = [123, 22, 78, 99, 108, 11, 1, 2]

    for _ in my_list:
        if _ % num == 0:
            print(_)
        else:
            continue


n = int(input("Enter a number: "))
check_diviibility = divisible(n)
print(check_diviibility)

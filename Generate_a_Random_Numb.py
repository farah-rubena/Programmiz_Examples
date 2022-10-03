# Python Program to Generate a Random Number

import random


def generate_random():

    x = random.randint(1, 101)
    return x


random_number = generate_random()
print(f"Random Number : {random_number}")

# Python Program to Convert Kilometers to Miles


def convert_km_to_miles(km):

    return km * 0.621


km = float(input("Enter total miles: "))
converted_miles = round(convert_km_to_miles(km), 2)
print(f"{km}km equals to {converted_miles}miles")

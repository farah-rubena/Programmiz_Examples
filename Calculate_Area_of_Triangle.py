#Python Program to Calculate the Area of a Triangle

def area_of_triangle(h, b):

    return h*b / 2

h = float(input("Enter a number: "))
b = float(input("Enter a number : "))
area = int(area_of_triangle(h,b))
print(f"Area of a Triamgle is {area}")
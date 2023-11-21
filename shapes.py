import math

"""
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {radius} is: {radius**2 * math.pi}")

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print(f"The area of the triangle with base {base} and height {height} is: {1/2 * base * height}")

length = float(input("Enter the length of the rectange: "))
breadth = float(input("Enter the breadth of the rectange: "))
print(f"The area of the rectangle with length {length} and breadth {breadth} is: {length*breadth}")

"""
def area_circle(radius):
    return radius**2 * math.pi

def area_triange(base, height):
    return 1/2 * base * height

def area_rectangle(length, breadth):
    return length*breadth

def square_perimenter(length):
    return length * 4

def circle_details(radius):
    circumference = 2 * math.pi * radius
    area = area_circle(radius)
    print(f"Circumference: {circumference:.2f}")
    print(f"Area: {area:.2f}")
    
circle_details(10)

def geometry(length, radius):
    square1 = square_perimenter(length)
    circle1 = 2 * math.pi * radius
    
    if square1 > circle1:
        print("Square has a larger perimeter")
    else:
        print("Cicle has a larger circumference")
        
    square2 = length ** 2
    circle2 = area_circle(radius)
    
    if square2 > circle2:
        print("Square has a larger area")
    else:
        print("Cicle has a larger area")
        
geometry(30, 15)
    
    
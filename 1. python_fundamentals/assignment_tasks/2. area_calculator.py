# ==================================================
# 2. Simple Area Calculator for Various Shapes
# ==================================================

# Step 1: Input shape choice from user
print("Calculate the area of the following shapes:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

# Circle area calculation
radius = float(input("\nEnter the radius of the circle: "))
pi = 3.141592653589793  
circle_area = pi * (radius ** 2)

# Rectangle area calculation
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_area = length * width

# Square area calculation
side = float(input("Enter the side length of the square: "))
square_area = side ** 2

# Triangle area calculation
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle_area = 0.5 * base * height

# Printing Results
print("\nResults:")
print(f"The area of the circle is: {circle_area:.2f}")
print(f"The area of the rectangle is: {rectangle_area:.2f}")
print(f"The area of the square is: {square_area:.2f}")
print(f"The area of the triangle is: {triangle_area:.2f}")

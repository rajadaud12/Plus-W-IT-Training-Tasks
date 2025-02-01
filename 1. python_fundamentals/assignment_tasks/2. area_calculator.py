# ==================================================
# 2. Simple Area Calculator for Various Shapes
# ==================================================

# Step 1: Input shape choice from user
print("Calculate the area of the following shapes:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")
shape = input("Enter the shape number (1-4): ")

# Step 2: Circle area calculation
if shape == "1":
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.141592653589793  
    area = pi * (radius ** 2)
    print(f"The area of the circle is: {area:.2f}")

# Step 3: Rectangle area calculation
elif shape == "2":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area:.2f}")

# Step 4: Square area calculation
elif shape == "3":
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area:.2f}")

# Step 5: Triangle area calculation
elif shape == "4":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f}")

else:
    print("Invalid shape choice!")

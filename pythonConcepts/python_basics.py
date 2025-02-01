# ==================================================
# Python Basics: Complete Program with Comments
# ==================================================

# 1. Indentation
if True:
    print("This is my second class of Python language") 




# 2. Comments
# if True:  # This line is commented out
#     print("This is my second class of Python language")




# 3. Variables and Constants
name = 'Daud'  # String 
age = 20        # Integer
PI = 3.14159    # Constant 

print("My name is", name)  
print("My age is", age)
print("Value of PI:", PI)



# 4. Input and Output Functions
name = input("Enter your name: ")  
print("My name is", name)          
print("Data type of name:", type(name))



# 5. Primitive Data Types
x = 10       # Integer
y = 10.01    # Float
z = 4 + 3j   # Complex number

print("Real part of z:", z.real)  # Access real part
print("Imaginary part of z:", z.imag)  # Access imaginary part




# 6. Strings
sentence = "This is my second class of Python language"

print("First letter:", sentence[0])  # Indexing
print("Character at index -15:", sentence[-15])  # Negative indexing

# Concatenation and repetition
greeting = "Python " + "language"  # Concatenation
repeat = "Python" * 3              # Repetition
print("Greeting:", greeting)
print("Repeated string:", repeat)

# Slicing
print("Sliced string (0:4):", sentence[0:4])  
print("Sliced string (0:23):", sentence[0:23])  

# String methods
print("Lower case:", sentence.lower())  # Convert to lowercase
print("Upper case:", sentence.upper())  # Convert to uppercase
print("Replace 'Python' with 'C++':", sentence.replace("Python", "C++"))  # Replace substring





# 7. Collection Data Types

# Lists: Ordered, mutable, allows duplicates
numbers = [1, 2, 3, 4, 5]
numbers.append(6) 
print("List:", numbers)
print("Sliced list (0:3):", numbers[:3])  

# Tuples: Ordered, immutable, allows duplicates
numbers_tuple = (1, 2, 3, 4, 5)
print("Tuple:", numbers_tuple)

# Sets: Unordered, mutable, no duplicates
numbers_set = {1, 2, 3, 4, 5}
numbers_set.add(5)  # Adding a duplicate has no effect
print("Set:", numbers_set)

# Dictionaries: Key-value pairs, unordered, mutable
student = {"name": "Daud"}  # Key-value pair
student['name'] = "Afnan"    # Update value
student['age'] = 20          # Add new key-value pair
print("Dictionary:", student)





# 8. Type Conversion

# Implicit Conversion: Python automatically converts data types
num1 = 10       # Integer
num2 = 10.01    # Float
result = num1 + num2  # Implicit conversion to float
print("Implicit conversion result:", result)
print("Data type of result:", type(result))

# Explicit Conversion: Manually convert data types
age = "20"      # String
integer = 10    # Integer
age = int(age)  # Convert string to integer
result = age + integer
print("Explicit conversion result:", result)






# 9. Operators

# Arithmetic Operators
num1 = 10
num2 = 4
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)  # num1 ^ num2

# Comparison Operators
print("Equal:", num1 == num2)
print("Not Equal:", num1 != num2)
print("Greater than:", num1 > num2)
print("Less than:", num1 < num2)

# Logical Operators
p = True
q = False
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

# Assignment Operators
a = 10
a += 5  # Equivalent to a = a + 5
a -= 5  # Equivalent to a = a - 5
a *= 5  # Equivalent to a = a * 5
a /= 5  # Equivalent to a = a / 5
print("Value of a after assignment operations:", a)





# 10. Common Functions

# Length Function
sentence = "Python"
print("Length of sentence:", len(sentence))  # Returns the length of the string

# Split Function
sentence = "Python:language"
print("Split sentence:", sentence.split(':'))  # Splits string into a list

# Random Functions
import random
print("Random integer between 1 and 10:", random.randint(1, 10))  # Random integer
print("Random float between 0 and 1:", random.random())  # Random float
print("Random choice from list:", random.choice(['Apple', 'Banana']))  # Random choice

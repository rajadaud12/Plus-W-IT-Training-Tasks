# ==================================================
# 1. Name Formatter and Length Calculator
# ==================================================

# Step 1: Input first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 2: Convert first name to uppercase and last name to lowercase
first_name = first_name.upper()
last_name = last_name.lower()

# Step 3: Calculate the sum of the letters
total_letters = len(first_name) + len(last_name)

# Step 4: Print the results
print(f"First name (upper): {first_name}")
print(f"Last name (lower): {last_name}")
print("Sum of letters in your first and last name:", total_letters)


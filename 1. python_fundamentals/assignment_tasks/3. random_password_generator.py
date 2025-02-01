
# ==================================================
# 3. Random Color-Based Password Generator
# ==================================================

def password_generator():
    import random

    # Step 1: Define the list of colors
    colors = ["red", "blue", "green", "yellow", "orange", "purple"]

    # Step 2: Generate a random index
    index = random.randint(0, len(colors) - 1)

    # Step 3: Select the color
    selected_color = colors[index]

    # Step 4: Reverse the selected color
    password = selected_color[::-1]

    # Step 5: Print the results
    print("Selected Color:", selected_color)
    print("Generated Password:", password)


# ==================================================
# Main Program Execution
# ==================================================

if __name__ == "__main__":
    
    print("\n===== Random Color-Based Password Generator =====")
    password_generator()
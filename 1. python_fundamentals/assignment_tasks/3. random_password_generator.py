# ==================================================
# 3. Random Color-Based Password Generator
# ==================================================

import random

# Step 1: Define the list of colors
colors = ["red", "black", "blue", "green", "yellow", "orange", "purple", "white"]

# Step 2: Generate a random index
index = random.randint(0, len(colors) - 1)

# Step 3: Select the color
selected_color = colors[index]

# Step 4: Reverse the selected color
password = selected_color[::-1]

# Step 5: Print the results
print("\n===== Random Color-Based Password Generator =====")
print("Selected Color:", selected_color)
print("Generated Password:", password)

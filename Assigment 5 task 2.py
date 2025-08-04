# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse these extracted elements
reversed_first_five = first_five[::-1]

# Optional: Use ANSI escape codes for colored output
pink = "\033[95m"
endc = "\033[0m"

print("Original list:", f"{pink}{numbers}{endc}")
print("Extracted first five elements:", f"{pink}{first_five}{endc}")
print("Reversed extracted elements:", f"{pink}{reversed_first_five}{endc}")

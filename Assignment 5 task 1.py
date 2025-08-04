# Step 1: Create a dictionary with student names and their marks
student_marks = {
    "Anil": 85,
    "Billa": 78,
    "Charan": 92,
    "Deyyam": 74
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show an appropriate message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the dictionary.")

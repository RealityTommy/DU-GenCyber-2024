'''
Student Grade Book Challenge
'''

# Initialize an empty dictionary to store student names and their grades
student_grades = {}

# Add a grade for a student
def add_grade(student_name, grade):

    # Check if student already has a grade
    if student_name in student_grades:
        print(student_name, "already has a grade.")

    else:
        student_grades[student_name] = grade
        print("Grade added for", student_name)

# Remove a grade for a student
def remove_grade(student_name):
    
    # Check if student already has a grade
    if student_name in student_grades:
        student_grades.pop(student_name)
        print(student_name, "grade removed.")

    else:
        print("This student is not in the grade book.")

# Display all student grades
def display_grades():
    
    # Check if there are any grades
    if student_grades:
        for student in student_grades:
            print(student, ":", student_grades[student])

    else:
        print("There are no grades yet.")

print("Welcome to the Student Grade Book!")

while True:
    print("\nOptions:")
    print("1. Add a student's grade")
    print("2. Remove a student's grade")
    print("3. Display all grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    print() # Display empty line for styling

    if choice == '4':
        print("Exiting...")
        break

    elif choice == '1':
        student_name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        add_grade(student_name, grade)

    elif choice == '2':
        student_name = input("Enter student name to remove grade: ")
        remove_grade(student_name)

    elif choice == '3':
        display_grades()

    else:
        print("Invalid input. Please enter a valid choice.")
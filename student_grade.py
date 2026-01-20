student_grades ={ }

def add_student(name, grade):
    student_grades[name]= grade
    print(f"Student {name} with a grade {grade} ")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student {name} updated with new grade {grade}")
    else:
        print(f"Student {name} not found.")

def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name} removed.")
    else:
        print(f"Student {name} not found.")

def view_student():
    print("Student Grades:")
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")

    else:
        print("No students found.")

def main():
    while True:
        operation = input("Do you want to add, update, remove, view or exit a student? (add/update/remove/view/exit): ").strip().lower()
        if operation == 'add':
            name = input("Enter the student's name: ")
            grade = input("Enter the student's grade: ")
            add_student(name, grade)

        elif operation == 'update':
            name = input("Enter the student's name to update: ")
            grade = input("Enter the new grade: ")
            update_student(name, grade)

        elif operation == 'remove':
            name = input("Enter the student's name to remove: ")
            remove_student(name)

        elif operation == 'view':
            view_student()

        elif operation == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    main()
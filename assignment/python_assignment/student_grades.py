students = {"Alice": "A", "Bob": "B"}  # Initial dictionary

while True:
    print("\nOptions:")
    print("1. Add new student")
    print("2. Update student grade")
    print("3. Print all students")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name} added successfully.")
    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated.")
        else:
            print("Student not found.")
    elif choice == 3:
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")

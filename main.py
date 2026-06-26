from student import create_student
from file_handler import save_student
from file_handler import view_students
from file_handler import search_by_qualification
from file_handler import load_students

while True:

    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. Search By Qualification")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        students = load_students()

        student = create_student(students)

        save_student(student)

        print("Student Added Successfully")

    elif choice == "2":

        search_by_qualification()

    elif choice == "3":

        view_students()

    elif choice == "4":

        print("Thank You")
        break

    else:

        print("Invalid Choice")
from file_handler import (
    students_registration,
    update_student,
    students_details,
    search_student)
while True:

    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. View All Students")
    print("5. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":

        students_registration()

    elif choice == "2":

        update_student()

    elif choice == "3":

        search_student()

    elif choice == "4":

        students_details()

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")
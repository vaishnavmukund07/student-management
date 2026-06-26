from datetime import datetime


def create_student(students):

    student_id = input("Enter Student ID: ")

    name = input("Enter Student Name: ")
    address = input("Enter Student Address: ")

    qualifications = []

    while True:

        qualification = input("Enter Qualification: ")
        qualifications.append(qualification)

        choice = input("Add another qualification? (y/n): ")

        if choice.lower() == "n":
            break

    student = {
        "student_id": student_id,
        "name": name,
        "address": address,
        "qualifications": qualifications,
        "create_date": str(datetime.now())
    }

    return student
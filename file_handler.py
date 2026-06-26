import json
FILE_NAME = "students_details.json"

def read_data():
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    return students
    
def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
    

def students_registration():

    students = read_data()

    student_id = input("Enter student id: ")
    student_name = (input("Enter student name: "))
    student_address = (input("Enter student address: "))

    qualifications = print("Enter the qualifications")

    skill = (input("Enter the skill: "))
    education = (input("Enter the highest qualification: "))
    year = int(input("Enter the passing year: "))

    student = {
        "student_id": student_id,
        "student_name": student_name,
        "student_address": student_address,
        "qualifications": {
            "skill": skill,
            "education": education,
            "year": year
        }
    }
    

    students.append(student)
    save_data(students)
    print("Student data saved successfully!")
    print("-----------------------------")


def update_student():
    student = input('Enter student name : ')
    students = read_data()

    for s in students:
        if s["student_name"].lower() == student.lower():
            new_student_address = str(input("Enter new address: "))
            qualifications = print("Enter the new qualifications")
            new_skill = str(input("Enter the new skill: "))
            new_education = str(input("Enter the new qualification: "))
            new_year = int(input("Enter the new passing year: "))

            s["student_address"] = new_student_address
            s["qualifications"]["skill"] = new_skill
            s["qualifications"]["education"] = new_education
            s["qualifications"]["year"] = new_year
            save_data(students)
            print("Student data updated successfully!")
            print("-----------------------------")
            return

    print("Student not found!")
def students_details():
    students = read_data()
    for student in students:
        print(student)
    print("------------------")


def search_student():
    search = input("Enter the student name to search:\n ")
    students = read_data()

    if len(students) == 0:
        print("Student not found!")
        return

    for student in students:
        print(f'student name: ', student["student_name"])
        print(f'student id: ', student["student_id"])
        print(f'student address: ', student["student_address"])
        print(f'student skill: ', student["qualifications"]["skill"])
        print(f'student education: ', student["qualifications"]["education"])
        print(f'student passing year: ', student["qualifications"]["passing_year"])

    print("----------------------")
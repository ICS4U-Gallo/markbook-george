"""
Markbook Application
Group members: Figo, Johnson
"""
from typing import Dict
import json

user = 0

def student_info_create():
    st_firstname = input("Please enter the student first name: ")
    st_lastname = input("Please enter the student last name: ")
    grade = input("Please enter the student grade: ")
    gender = input("Please enter the student gender: ")
    st_number = input("Please enter the student number: ")
    studentx = {
        "Student Firstname": st_firstname,
        "Student Lastname": st_lastname,
        "Grade": grade,
        "Gender": gender,
        "Assignment List": []
    }
    if input("are you sure? enter y or n y:yes n:no: ") == "y":
        write_to_student(st_number, studentx)


def write_to_student(st_number, new_student: dict):
    with open("save_information.json", 'r') as json_file:
        data = json.load(json_file)
        data["student"][st_number] = new_student
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile)


def create_assignment() -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    course_code = input("Please enter the course code of this assignment: ")
    name = input("Please enter the assignment name: ")
    due = input("Please enter the due date: ")
    points = input("Please enter what the assignment is out of: ")
    course_code = input("Please enter the course code: ")
    if input("are you sure? enter y or n y:yes n:no: ") == "y":
        write_to_assignment(course_code, {
            "name": name,
            "due": due,
            "points": points,
            "course_code": course_code
        })


def write_to_assignment(course_code, new_assignment: dict):
    with open("save_information.json", 'r') as json_file:
        data = json.load(json_file)
        data["assignment"][course_code] = (new_assignment)
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile)


def create_classroom():
    course_code = input("enter coursecode: ")
    course_name = input("enter course name: ")
    period = int(input("enter period: "))
    teacher = input("enter teacher: ")
    """Creates a classroom dictionary"""
    if input("are you sure? enter y or n y:yes n:no: ") == "y":
        write_to_classroom(course_code, {
            "CourseName": course_name,
            "Period": period,
            "Teacher": teacher,
            "student_list": []
        })


def write_to_classroom(course_code, new_classroom: Dict):
    with open("save_information.json", 'r') as json_file:
        data = json.load(json_file)
        data["classroom"][course_code] = new_classroom
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile)


def calculate_average_mark(student):
    """Calculates the average mark of a student"""
    marks = student["marks"]
    total = 0
    ave = 0
    for mark in strudent["marks"]:
        total += int(mark)
    ave = total / len(student["marks"])
    return ave


def add_student_to_classroom():
    student_number = input("enter student number: ")
    course_code = input("enter the course code: ")
    if input("are you sure? enter y or n y:yes n:no: ") == ("y"):
        write_to_course_studentlist(student_number, course_code)
        pass


def write_to_course_studentlist(reg_student_id, course_code):
    with open("save_information.json", "r") as json_file:
        data = json.load(json_file)
        for value in data.values():
            for key in value.keys():
                if key == reg_student_id:
                    data["classroom"][course_code]["student_list"].append(
                        reg_student_id)
            #for student in data["student"]:
            #if data["students"]["studentID"]==reg_student_id:
            #data["students"]["studentID"]["courses"].append(course_code)
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile)


def remove_student_from_classroom():
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    st_number = input("Please enter the student's code you want to delete: ")
    course_code = input("Please enter the course code that you want to remove the student from: ")
    with open("save_information.json", "r") as json_file:
        data = json.load(json_file)
        if input("are you sure? enter y or n y:yes n:no: ") == ("y"):
            data["classroom"][course_code]["student_list"].remove(st_number)
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile)
    pass


def edit_student():
    """Edits the student's info with the provided key/value pairs
    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    st_number = input("Please enter the student's number you want to edit with: ")
    st_firstname = input("Please enter the student first name: ")
    st_lastname = input("Please enter the student last name: ")
    grade = input("Please enter the student grade: ")
    gender = input("Please enter the student gender: ")
    studentx = {
        "Student Firstname": st_firstname,
        "Student Lastname": st_lastname,
        "Grade": grade,
        "Gender": gender,
        "Assignment List": []
    }

    studenty = {
        "Student Firstname": st_firstname,
        "Student Lastname": st_lastname,
        "Grade": grade,
        "Gender": gender,
    }
    with open("save_information.json", "r") as json_file:
        data = json.load(json_file)
        for value in data.values():
            for key in value.keys():
                if key == st_number:
                    if input("Do you want to reset the Assignment of this student as well? 'y' for Yes and n for 'No'") == ("y"):
                        data["student"][st_number].update(studentx)
                    else:
                        data["student"][st_number].update(studenty)
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile) 

    pass


def update_student_mark():
    st_number = input("Please enter the student number: ")
    with open("save_information.json", "r") as json_file:
        data = json.load(json_file)
        while True:
            try:
                st_mark = float(input("Please enter the student's mark: "))
            except:
              print("OOPs! Please enter a number\n")
            data["student"][st_number]["Assignment List"].append(st_mark)
            decide = input("Enter 'P' to stop\nPress SPACE to coutinue").upper()
            if decide == "P":
                break
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile) 


        



    

def main():
    global user
    print("\nWelcome! to our markbook!")
    while True:
        print("[0]-create a classroom\n"
              "[1]-create assignemt\n"
              "[2]-calculate average mark\n"
              "[3]-create student\n"
              "[4]-add student to classroom\n"
              "[5]-remove a student from a class\n"
              "[6]-edit a student information\n"
              "[7]-update a student's mark")
        user = int(input("Please enter a number from above\n-> "))

        if user == 0:
            create_classroom()

        if user == 1:
            create_assignment()

        if user == 2:
            calculate_average_mark()

        if user == 3:
            student_info_create()

        if user == 4:
            add_student_to_classroom()

        if user == 5:
            remove_student_from_classroom()

        if user == 6:
            edit_student()

        if user == 7:
            update_student_mark()

main()

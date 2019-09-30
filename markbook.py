"""
Markbook Application
Group members: Figo, Johnson
"""
from typing import Dict
import json

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
    print("\nSuccessful Created\n")


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
    print("\nSuccessful Created\n")


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
    print("\nSuccessful Created\n")


def calculate_average_mark():
    """Calculates the average mark of a student"""
    st_number = input("Please enter the student number: ")
    with open("save_information.json", 'r') as json_file:
        data = json.load(json_file)
        ave = 0
        for marks in data["student"][st_number]["Assignment List"]:
            ave += marks
        ave = ave/len(data["student"][st_number]["Assignment List"])
    print(
        "The Student with the Student Code: "
        + str(st_number) +"\n"
        "Has a average mark with: " + str(ave)
    )


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
                    try: data["classroom"][course_code]["student_list"]    .append(reg_student_id)
                    except:
                        print("OPPS! Looks like you enter something wrong!")
                        break
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile)


def remove_student_from_classroom():
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
                    if input("Do you want to reset the Assignment of this student as well? 'Y' for Yes and 'N' for 'No'").upper() == ("Y"):
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


def reset_everything():
    decide = input(
        "Are you sure you want to DELETE everything you saved?\n"
        "Enter 'YES' properly to confirm your choice\n"
        "Enter 'No' to cancle this process: "
    ).upper()
    with open("save_information.json", "r") as json_file:
        data = json.load(json_file)
        if decide == "YES":
            data = {
                "student": {},
                "classroom": {},
                "assignment": {}
            }
    with open("save_information.json", 'w') as outfile:
        json.dump(data, outfile) 
    print("\nSuccessful Reset!\n")



    

def main():
    print("\nWELCOME! TO OUR MARKBOOK!")
    while True:
        print(
            "\n[1]-Management Classroom\n"
            "[2]-Management Assignment\n"
            "[3]-Management Student\n"
            "[4]-RESET EVERYTHING!\n"
        )
        try:
            user = int(input("Please enter a number from above\n->> "))
        except:
            print("Please enter an integer number from above")

        if user == 1:
            print(
                "\n[1]-Create a Classroom\n"
                "[2]-Add a Student to a Classroom\n"
                "[3]-Remove a Student from a Classroom\n"
            )
            try:
                cuser = int(input("Please enter a number from above\n->> "))
            except:
                print("Please enter an integer number from above")

            if cuser == 1:
                create_classroom()
            if cuser == 2:
                add_student_to_classroom()
            if cuser == 3:
                remove_student_from_classroom()

        if user == 2:
            print(
                "\n[1]-Create an Assignment\n"
            )
            try:
                auser = int(input("Please enter a number from above\n->> "))
            except:
                print("Please enter an integer number from above")

            if auser == 1:
                create_assignment()
        
        if user == 3:
            print(
                "\n[1]-Create a Student\n"
                "[2]-Add a Student to a Classroom\n"
                "[3]-Remove a Student from a Classroom\n"
                "[4]-Calculate a Student's Average Mark\n"
                "[5]-Edit a Student's Information\n"
                "[6]-Update a Student's Mark\n"
            )
            try:
                suer = int(input("Please enter a number from above\n->> "))
            except:
                print("Please enter an integer number from above")

            if suer == 1:
                student_info_create()
            if suer == 2:
                add_student_to_classroom()
            if suer == 3:
                remove_student_from_classroom()
            if suer == 4:
                calculate_average_mark()
            if suer == 5:
                edit_student()
            if suer == 6:
                update_student_mark()

        if user == 4:
            reset_everything()

main()

"""
Markbook Application
Group members: Figo, Johnson, Geroge
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {"name": name, "due": due, "points": points}


def create_classroom(course_code, course_name, period, teacher):
    """Creates a classroom dictionary"""
    return {"CourseCode": couse_code, "CourseName": couse_name, "Period": 3, 
    "Teacher": teacher, "student_list": []}


def calculate_average_mark(student):
    """Calculates the average mark of a student"""
    marks = student["marks"]
    total = 0
    ave = 0
    for mark in strudent["marks"]:
        total += int(mark)
    ave = total/len(student["marks"])
    return ave


def add_student_to_classroom(student, classroom):
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom["student_list"].append(student)
    pass


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    calssroom["student_list"].pop(index(student))
    pass


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs
    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """

    pass

while True: 
    menu = "menu"
    if menu == "menu":
        print("Type 'assignment' to create an assignment")
        print("Type 'classroom' to create a classroom")
        print("Type 'mark' to calculate average mark")
        print("Type 'Astudent' to add student to classroom")
        print("Type 'Rstudent' to remove student from cmenulassroom")
        print("Type 'Estudent' to edit student in classroom")
        menu = input()

    if menu == "assignment":
        create_assignment()
        print("Type 'menu' to get back to menu")
        menu = input()

    if menu == "classroom":
        create_classroom()
        print("Type 'menu' to get back to menu")
        menu = input()

    if menu == "mark":
        calculate_average_mark()
        print("Type 'menu' to get back to menu")
        menu = input()

    if menu == "Astudent":
        add_student_to_classroom()
        print("Type 'menu' to get back to menu")
        menu = input()

    if menu == "Rstudent":
        remove_student_from_classroom()
        print("Type 'menu' to get back to menu")
        menu = input()

    if menu == "Estudent":
        edit_student()
        print("Type 'menu' to get back to menu")
        menu = input()



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
    return {"CourseCode": couse_code, "CourseName": couse_name, "Period": period, "Teacher": teacher}


def calculate_average_mark(student):
    """Calculates the average mark of a student"""
    marks = student["marks"]
    total = 0
    for mark in marks:
        total
    return 0

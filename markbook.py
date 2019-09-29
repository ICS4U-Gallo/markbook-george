"""
Markbook Application
Group members: Figo, Johnson
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int,course_code:int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {"name": name, "due": due, "points": points , "course_code":int}


def create_classroom():
    course_code=input("enter coursecode")
    course_name=input("enter course name")
<<<<<<< HEAD
    period = int(input("enter period"))
    teacher = input("enter teacher")
    """Creates a classroom dictionary"""
    if input("are you sure? enter y or n y:yes n:no").equals("y"):
        write_to_classroom({"CourseCode": couse_code, "CourseName": couse_name, "Period": period,
=======
    #and so on
    """Creates a classroom dictionary"""
    if input("are you sure? enter y or n y:yes n:no").equals("y"):
        write_to_classroom({"CourseCode": couse_code, "CourseName": couse_name, "Period": 3,
>>>>>>> a35124c051077b9ece608d2838894f8b18b33731

            "Teacher": teacher, "student_list": [], "assignment_list": []})


def write_to_classroom(new_classroom:Dict):
    file_name=get_file_name()
    with open(file_name) as json_file:
        data = json.load(json_file)
        data["classroom"].append(new_classroom)
    nfile_name=getn_file_name()
    with open(nfile_name, 'w') as outfile:
            json.dump(data, outfile)


def calculate_average_mark(student):
    """Calculates the average mark of a student"""
    marks = student["marks"]
    total = 0
    ave = 0
    for mark in strudent["marks"]:
        total += int(mark)
    ave = total/len(student["marks"])
    return ave


def add_student_to_classroom():
    studen_id=input("enter student id")
    course_code=input("enter the course code")
    # get input for both arguments!!!
<<<<<<< HEAD
    if input("are you sure? enter y or n y:yes n:no") == ("y"):

        write_to_course_studentlist(student_id, course_code)
=======
    if input("are you sure? enter y or n y:yes n:no").equals("y"):

        write_to_course_studentlist(student_id:int, course_code:int)
>>>>>>> a35124c051077b9ece608d2838894f8b18b33731

        pass

def write_to_course_studentlist(reg_student_id ,course_code):
    file_name=get_file_name()
    with open(file_name) as json_file:
        data = json.load(json_file)
        if data["studentIDList"].contains(reg_student):
            data["classrooms"][reg_class_room]["courseStudentIDList"].append(reg_student)
            for student in data["student"]:
                if data["students"]["studentID"]==reg_student_id:
                    data["students"]["studentID"]["courses"].append(course_code)
    nfile_name=getn_file_name()
    with open(nfile_name, 'w') as outfile:
            json.dump(data, outfile)


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

    if menu =="UGstudent":
        update_student_mark()




class Student:
    def __init__(self,st_name,st_lastname, gender, image, st_number, email, assignment):
        self.st_name = st_name
        self.st_lstname = st_lastname
        self.gender = gender
        self.image = image
        self.st_number = st.st_number
        self.email = email
        self.assignment = assignment

    def get_name(self ,name):
        return(st_name)

    def get_lastname(self, lastname):
        return(st_lastname)

    def get_gender(self, gender):
        return(gender)

    def get_image(self, image):
        return(image)

    def get_number(self, number):
        return(st_number)

    def get_email(self, email):
        return(email)

    def update_st(self,st_name ,st_lastname, gender, image, st_number, email, assignment):
        self.st_name = st_name
        self.st_lstname = st_lastname
        self.gender = gender
        self.image = image
        self.st_number = st.st_number
        self.email = email
        self.assignment = assignment




    def save_grade(self, assignment_name , st_grade):
        self.assignment_name = assignment_name
        self.grade = st_grade


class Classroom:
    def __init__(self, course_code, teacher_name, period, student_list):
        self.course_code = course_code
        self.teacher_name = teacher_name
        self.period = period
        self.student_list = student_list


def student_info_create():
<<<<<<< HEAD
=======

    st_name = input("enter the student name")

    st_id=input("enter the student id") #and so on

    studentx = {"studentname": st_name, "student_lasyname": st_lname ,...}


def write_to_listAllStudents(new_student:Dict):
    file_name=get_file_name()
    with open(file_name) as json_file:
        data = json.load(json_file)
        data["students"].append(new_student)
        data["studentIDList"].append(new_student['student_id'])
    nfile_name=getn_file_name()
    with open(nfile_name, 'w') as outfile:
            json.dump(data, outfile)
    

#question:how to specify which assignment is for what classroom

def update_student_mark():
    inp_number=input("enter the student name")
    course_code=input()
    assignment_name=
    grade=input()
    for classroom in class_list:
        if class_list[classroom]["student_list"][st_number]==inp_number:
            class_list[classroom]["student_list"]["assigment_list"]["assignment_name"]=grade

>>>>>>> a35124c051077b9ece608d2838894f8b18b33731

    st_firstname = input("enter the student first name")
    st_lastname = input("enter the student last name")
    st_id=input("enter the student id")
    studentx = {"studentname": st_firstname, "student_lasyname": st_lastname, "studentID": st_id}
    write_to_listAllStudents(studentx)

<<<<<<< HEAD
def write_to_listAllStudents(new_student:Dict):
    file_name=get_file_name()
    with open(file_name) as json_file:
        data = json.load(json_file)
        data["students"].append(new_student)
        data["studentIDList"].append(new_student['student_id'])
    nfile_name=getn_file_name()
    with open(nfile_name, 'w') as outfile:
            json.dump(data, outfile)
    

=======
"student_list": []
#save dictionaries and information into the json file

def first_write_to_file(str filepath , studententery ,..):
    if studententery notnull
    write_to student

    write_to_classroom()



def write_to_class():
    create_classroom()
>>>>>>> a35124c051077b9ece608d2838894f8b18b33731

def update_student_mark():
    inp_number=input("enter the student name")
    course_code=input("enter the course code")
    assignment_name= ("enter the assignment name")
    grade=input()
    for classroom in class_list:
        if class_list[classroom]["student_list"][st_number]==inp_number:
            class_list[classroom]["student_list"]["assigment_list"]["assignment_name"]=grade



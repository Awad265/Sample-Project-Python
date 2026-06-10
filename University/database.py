"""Simple databade IO for university"""

from student import Student
from course import Course

STUDENT_DATABASE = "./data/students.csv"

#student: id, name, course1, course2: mark

def write_student(student):

    with open(STUDENT_DATABASE, "a") as f:
        s = f"{student.id},{student.name}"

        for k,v in student.courses.items():
            s += f",{k}:{v}"

        s += "\n"

def main():

    s1.student("")

     

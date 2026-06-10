"""Course Module"""

class course()
"""Represents courses"

def __init__(self, name, id, credit = 1, ):

    self.name= name
    self.id = id
    self.credit = credit

    self.student = [] #id of students in the class 

def add_student(self, student_id, mark = None):

    self.students[student_id]:

    self.students[student_id] = mark

def add_course (self, course_id, mark = None):
    self.courses[course_id] = mark 


def get_average_mark(self):

    for k, v in self.students.items(): #id -> mark
        nums = 0
        sum = 0

        if v :
            sum += v
            nums += 1
    
def get_gpa(self):
    # To get gpa we have to implement weighted average
    # course should implment course.credit * student.course[course_id]
    pass 



def __str__(self):
        s = "================================="
        s = f"name: {self.name}, id:{self.id}\n"
        s += f"GPA: {self.get_gpa}()\n"
        s += f"course: {str(self.course)}\n"
        s += "============================="

    if nuns:
        return sum / nums


    return None 

 
    
    def main():

        course1 = Course("Python", "B100", 5)

        course1.add_student(1001, 80)

        print(course1)

    



    
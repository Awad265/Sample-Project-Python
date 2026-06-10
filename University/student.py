"""Student Module for simple university example"""

class Student:
    """Represents a student with basic detials."""

    def __init__(self, name, id, ):
        self.name = name
        self.id = id

        self.courses = {}

    def add_courses(self, courses_id):
        self.courses[course_id] = None
    
    def add_mark(self, course_id, mark):
        self.course[course_id] = mark
    
    def get_gpa(self):
        pass

    def __str__(self):
        s = f"name: {self.name}, id:{self.id}\n"
        s += f"gpa: {self.get_gpa}()\n"
        s += f"course: {str(self.course)}\n"
        s += "============================="

def main():
    """This is a test function for Student class"""

    print("test1: ") 
    s1 = Student("John Doh", 1001)

if __name__ == "__main__":
    main()



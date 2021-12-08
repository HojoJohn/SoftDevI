"""
A Student class.

@author GCCIS Faculty
"""

GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F", "NG"]

QUALITY_POINTS = {
    GRADES[0]: 4.0,
    GRADES[1]: 3.67,
    GRADES[2]: 3.33,
    GRADES[3]: 3.0,
    GRADES[4]: 2.67,
    GRADES[5]: 2.33,
    GRADES[6]: 2.0,
    GRADES[7]: 1.67,
    GRADES[8]: 1.0,
    GRADES[9]: 0,
    GRADES[10]: 0 # no grade
}

class Student:
    """
    A class that represents a student with fields for ID, name, credits, and
    GPA.
    """
    __slots__ = ["__id", "__name", "__credits", "__gpa"]

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0

    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credits
    def get_gpa(self):
        return self.__gpa
    def get_id(self):
        return self.__id

    def print_student(self):
        """
    Prints a student's info to standard output.
    """
        print("Student: ID=",self.__id, ", name=", self.__name, 
        ", credits=", self.__credits, ", GPA=", self.__gpa,sep="")

    def make_student(id,name):
        student = Student()
        student.id = id
        student.name = name
        return student
    def add_course(self,id,name, course):
        student = make_student(id, name)
        self.__course += [course]
        self.__credits += course.get_credit()

    """
    def add_course(self,course):
    
        self.__courses += [course]
        self.__credits += course.get_credits()
    
    """
    def get_student(id,population):

        if id in population:
            student = population[id]
            return student
        else:
            return None
    
    def get_credits(id,population):
        student = get_student(id,population)
        if student is not None:
            return student.credits
        else:
            return None
    
    def get_gpa(self):
        total_quality_points = 0
        total_credits = 0

        for course in self.__courses:
            total_credits += course.get_credits
            total_quality_points += QUALITY_POINTS[course.get_grades()] * course.get_credits
        
        if total_credits == 0:
            return 00

        else:
            return total_quality_points / total_credits




class Course:

    __slots__ = [ '__id', '__name','__credits','__courses']

    def __init__(self,name,credits,grades):
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0

        self.__courses = []
    
    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits
    def get_grades(self):
        return self.__grades

    def print_courses(self):
        student1 = Student('456-DEF', 'Harris')

        print("Student Name:",self.get_name,"credtis=",self.get_credits,"grades=",self.get_grades)

class Student:
    __slots__ =['id','name','credits', 'gpa']
    a_list = [1,2,3,4]

    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0.0
       

    

def print_student(student):

    print("student:",student.id, ',', student.name, ',', student.credits, ',', student.gpa)

def make_student(id,name):
    student = Student()
    student.id = id
    student.name = name
    return student

def add_student(id,name,population):
    student = make_student(id,name)
    population[id] = student

def get_student(id,population):
    if id in population:
        student = population[id]
        return student
    else:
        return None
def get_credits(id,population):
    student = get_student(id,population)

    if student is not None:
        student.credits += credits

def get_credits(id,population):
    student = get_student(id,population)

    if student is not None:
        return student.credits
    else:
        return None
def main():

    student1 = Student()
    student2 = Student()

    student1 = Student("123-ABC", "Charlie Brown")
    student2 = Student("456-DEF","Brian Stevens")

    print("Student1:",student1.id, ',', student1.name,',',student1.credits, ',', student1.gpa,student1.a_list)
    print("Student2:",student2.id, ',', student2.name,',',student2.credits, ',', student2.gpa,student2.a_list)

    student1.a_list[0] = 4
    print("Student1:",student1.id, ',', student1.name,',',student1.credits, ',', student1.gpa,student1.a_list)
    print("Student2:",student2.id, ',', student2.name,',',student2.credits, ',', student2.gpa,student2.a_list)

    student1.id = "123-abc"
    student1.name = "Charlie Brown"
    student1.credits = 34
    student1.gpa = 2.3

main()
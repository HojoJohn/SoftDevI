import students


def main():

    student = students.Student("TCMVSE", "Thomas Maszerowski")
    print("Student: ID=",student.get_id(), ", name=", student.get_name,
        ", credits=", student.get_credit, ", GPA=", student.get_gpa, sep="")

    student.print_student()

main()
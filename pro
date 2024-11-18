class University:
    def __init__(self):
        self.students = []
        self.professors = []
        self.available_courses = ["Math", "Computer Science", "Physics", "Chemistry"]

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"Student {student.name} has been added to the university.")
        else:
            print("Only Student instances can be added as students.")

    def add_professor(self, professor):
        if isinstance(professor, Professor):
            self.professors.append(professor)
            print(f"Professor {professor.name} has been added to the university.")
        else:
            print("Only Professor instances can be added as professors.")

    def enroll_student_in_course(self, student, course):
        if course in self.available_courses:
            student.enroll_in_course(course)
        else:
            print(f"Error: Course '{course}' is not available at the university.")

    def assign_professor_to_course(self, professor, course):
        if course in self.available_courses:
            professor.assign_subject(course)
        else:
            print(f"Error: Course '{course}' is not available at the university.")

    def display_all_students(self):
        print("\nAll Students:")
        if self.students:
            for student in self.students:
                print(student.display_info())
        else:
            print("No students enrolled.")

    def display_all_professors(self):
        print("\nAll Professors:")
        if self.professors:
            for professor in self.professors:
                print(professor.display_info())
        else:
            print("No professors assigned.")

    def display_totals(self):
        print(Student.total_students_count())
        print(Professor.total_professors_count())
        print(Person.total_people_count())


# Creating university
uni = University()

# Creating students
student1 = Student("Ali", 20, "S001", "123 Main St", (38, 98))
student2 = Student("Noor", 22, "S002", "456 Oak St", (93, 80))

# Adding students to university
uni.add_student(student1)
uni.add_student(student2)

# Enrolling students in courses
uni.enroll_student_in_course(student1, "Math")
uni.enroll_student_in_course(student1, "Biology")  # Invalid course
uni.enroll_student_in_course(student2, "Physics")

# Creating professors
prof1 = Professor("Dr. Smith", 45, "P001")
prof2 = Professor("Dr. Jones", 50, "P002")

# Adding professors to university
uni.add_professor(prof1)
uni.add_professor(prof2)

# Assigning professors to courses
uni.assign_professor_to_course(prof1, "Math")
uni.assign_professor_to_course(prof2, "Chemistry")
uni.assign_professor_to_course(prof2, "Astronomy")  # Invalid course

# Display all students and professors
uni.display_all_students()
uni.display_all_professors()
uni.display_totals()


from abc import ABC,abstractmethod

class Person(ABC):
    total_people = 0

    def init(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1

    @classmethod
    def total_people_count(cls):
        return f"Total people (students and professors): {cls.total_people}"

    @abstractmethod
    def display_info(self):
        pass

class Student(Person):
    total_students = 0

    def init(self, name, age, student_id, address, grades, courses=None):
        super().init(name, age)
        self.student_id = student_id
        self.address = address
        self.grades = grades
        self.courses = courses if courses is not None else []
        Student.total_students += 1

    def enroll_in_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course}")


    def get_grades(self):
        return self.__grades

    def is_passed(self):
        return "Passed" if self.__grades[0] >= 50 else "Failed"


    def display_info(self):
        course_list = ', '.join(self.courses) if self.courses else "No courses enrolled"
        return f"{super().display_info()}, Student ID: {self.student_id}, Address: {self.address}, Courses: {course_list}, Grades: {self.__grades}, Status: {self.is_passed()}"


    @classmethod
    def total_students_count(cls):
        return f"Total students: {cls.total_students}"



class Professor(Person):
    total_professors = 0

    def __init(self, name, age, professor_id, subjects=None):
        super().init(name, age)
        self.professor_id = professor_id
        self.subjects = subjects if subjects is not None else []
        Professor.total_professors += 1

    def assign_subject(self, subject): # اضافة مادة جديدة
        self.subjects.append(subject)
        print(f"{self.name} has been assigned to teach {subject}")

    def display_info(self):
        subject_list = ', '.join(self.subjects) if self.subjects else "No subjects assigned"
        return f"{super().display_info()}, Professor ID: {self.professor_id}, Subjects: {subject_list}"


    @classmethod
    def total_professors_count(cls):
        return f"Total professors: {cls.total_professors}"


class University:
    def init(self):
        self.students = []
        self.professors = []

    def add_student(self, student):
        if isinstance(student,Student):
         self.students.append(student)
         print(f"Student {student.name} has been added to the university.")
        else:
            print("only Student instance can be added as student.")

    # Add a professor to the university
    def add_professor(self, professor):
        if isinstance(professor,Professor):
         self.professors.append(professor)
         print(f"Professor {professor.name} has been added to the university.")
        else:
            print("only Professor instance can be added as professor.")

    def display_all_students(self):
        print("\nAll Students:")
        if self.students:
         for student in self.students:
            print(student.display_info())
        else:
            print("no students enrolled.")

    def display_all_professors(self):
        if self.professors:
         print("\nAll Professors:")
        for professor in self.professors:
            print(professor.display_info())
        else:
            print("no professor assigned ")


    def display_totals(self):
        print(Student.total_students_count())
        print(Professor.total_professors_count())
        print(Person.total_people_count())

# Creating university
uni = University()

# Creating students
student1 = Student("Ali", 20, "S001", "123 Main St", (75,98), ["Math", "Computer Science"])
student2 = Student("noor", 22, "S002", "456 Oak St", (45,80), ["Physics", "Chemistry"])

# Adding students to university
uni.add_student(student1)
uni.add_student(student2)

# Creating professors
prof1 = Professor("Dr. Smith", 45, "P001", ["Math", "Physics"])
prof2 = Professor("Dr. Jones", 50, "P002", ["Chemistry"])
# Adding professors to university
uni.add_professor(prof1)
uni.add_professor(prof2)

# Display all students and professors
uni.display_totals()

print(f"name:0{student1.name}")
print(f"Student ID: {student1.student_id}")
print(f"Grades :{student1.get_grades()}")
print(f"Status:{student1.is_passed()}")

print(f"name:{student2.name}")
print(f"Student ID: {student2.student_id}")
print(f"Grades :{student2.get_grades()}")
print(f"Status:{student2.is_passed()}")
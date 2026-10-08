# ============================================================
# Student Management System
# OOP Concepts: Class & Object, Attributes, Methods,
# Inheritance, Polymorphism, Method Overriding,
# Method Overloading, Encapsulation
# ============================================================


# ============================================================
# 1. Student Class (Base Class)
# ============================================================

class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.department = department
        self.__email = email        # Encapsulation: private attribute
        self.__marks = []           # Encapsulation: private attribute

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
        else:
            print("Invalid email!")

    def add_marks(self, *args):
        for mark in args:
            self.__marks.append(mark)

    def calculate_result(self, passing_mark=40):
        if not self.__marks:
            return "No marks added."
        average = sum(self.__marks) / len(self.__marks)
        status = "Pass" if average >= passing_mark else "Fail"
        return f"Average: {average:.2f} | Status: {status}"

    def get_student_type(self):
        return "General Student"

    def display_info(self):
        print("=" * 40)
        print(f"Name        : {self.name}")
        print(f"Student ID  : {self.student_id}")
        print(f"Email       : {self.__email}")
        print(f"Age         : {self.age}")
        print(f"Department  : {self.department}")
        print(f"Type        : {self.get_student_type()}")
        print(f"Result      : {self.calculate_result()}")
        print("=" * 40)


# ============================================================
# 2. UndergraduateStudent Class
# ============================================================

class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    def get_student_type(self):
        return f"Undergraduate Student - Semester {self.semester}"

    def display_info(self):
        super().display_info()
        print(f"Semester    : {self.semester}")
        print("=" * 40)


# ============================================================
# 3. GraduateStudent Class
# ============================================================

class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def get_student_type(self):
        return f"Graduate Student - Research: {self.research_topic}"

    def display_info(self):
        super().display_info()
        print(f"Research    : {self.research_topic}")
        print("=" * 40)


# ============================================================
# Main
# ============================================================

ug_student = UndergraduateStudent("Shraboni Roy", "UG-2024-001", "shraboni@university.edu", 20, "CSE", 2)
grad_student = GraduateStudent("Nadia Sultana", "GR-2024-042", "nadia@university.edu", 25, "CSE", "Machine Learning")

ug_student.add_marks(72, 85, 90, 68)
grad_student.add_marks(88, 91, 95, 78, 84)

print("\n--- Undergraduate Student ---")
ug_student.display_info()

print("\n--- Graduate Student ---")
grad_student.display_info()

print("\n--- Polymorphism Demo ---")
for s in [ug_student, grad_student]:
    print(f"{s.name} => {s.get_student_type()}")

print("\n--- Encapsulation Demo ---")
print(f"Email: {ug_student.get_email()}")
ug_student.set_email("arif.updated@university.edu")
print(f"Updated Email: {ug_student.get_email()}")

print("\n--- Method Overloading Demo ---")
print(f"Result (passing=50): {ug_student.calculate_result(passing_mark=50)}")
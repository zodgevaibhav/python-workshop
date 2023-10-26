class Student:
    schoolName = "XYZ School"  # Class-level (static) variable
    def get_full_name(self):
        return f"{self.firstName} {self.lastName}"

    def __init__(self, first_name, last_name, roll_number, standard):
        self.firstName = first_name
        self.lastName = last_name
        self.rollNumber = roll_number
        self.standard = standard

    @staticmethod  # Static method (no access to instance variables)
    def get_school_name():
        return Student.schoolName

    def print_student_info(self):
        student_full_name = self.get_full_name()  # Local variable
        print(f"Student Info:")
        print(f"Name: {student_full_name}")
        print(f"Roll Number: {self.rollNumber}")
        print(f"School: {Student.schoolName}")


std = Student("John", "Doe", "S12345", "10")  # Create a Student object
full_name = std.get_full_name()
std.print_student_info()
school = Student.get_school_name()  # Static Method call
print(f"{full_name} attends {school}.")  # Output

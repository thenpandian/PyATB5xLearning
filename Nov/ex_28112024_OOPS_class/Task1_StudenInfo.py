class Batch1:
    # Parametrized constructor to set the values of the attributes
    def __init__(self, student_name, student_id, course, batch_time, grade):
        self.student_name = student_name
        self.student_id = student_id
        self.course = course
        self.batch_time = batch_time
        self.grade = grade

    # Method to print student information
    def print_student_info(self):
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Batch Time: {self.batch_time}")
        print(f"Grade: {self.grade}")

    # Method to update student grade
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Grade for {self.student_name} has been updated to {self.grade}")

    # Method to change batch time
    def change_batch_time(self, new_batch_time):
        self.batch_time = new_batch_time
        print(f"Batch time for {self.student_name} has been changed to {self.batch_time}")


# Example of how to use the class
student1 = Batch1("John Doe", "S12345", "Python Programming", "9 AM - 11 AM", "A")
student1.print_student_info()

# Update grade and batch time
student1.update_grade("A+")
student1.change_batch_time("11 AM - 1 PM")

# Print updated student information
student1.print_student_info()
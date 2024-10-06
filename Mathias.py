class University:
    def __init__(self):
        # Dictionaries to store student, course, and lecturer details
        self.students_data = {}
        self.courses_data = {}
        self.lecturers_data = {}

    def students(self, student_id, name, age, course):
        """Function to add or update student details"""
        self.students_data[student_id] = {
            'name': name,
            'age': age,
            'course': course
        }
        return f"Student {name} has been added/updated."

    def courses(self, course_id, course_name, lecturer):
        """Function to add or update course details"""
        self.courses_data[course_id] = {
            'course_name': course_name,
            'lecturer': lecturer
        }
        return f"Course {course_name} has been added/updated."

    def lecturers(self, lecturer_id, lecturer_name, department):
        """Function to add or update lecturer details"""
        self.lecturers_data[lecturer_id] = {
            'lecturer_name': lecturer_name,
            'department': department
        }
        return f"Lecturer {lecturer_name} has been added/updated."

    def get_students(self):
        """Function to get all students"""
        return self.students_data

    def get_courses(self):
        """Function to get all courses"""
        return self.courses_data

    def get_lecturers(self):
        """Function to get all lecturers"""
        return self.lecturers_data


# Example
university = University()

# Adding students
print(university.students(1, "Mathias", 30, "Computer Science"))
print(university.students(2, "September", 22, "Information Technology"))

# Adding courses
print(university.courses(101, "Object Oriented Programming", "Dr. Kasozi"))
print(university.courses(102, "Advanced Ethics", "Rev. Footi"))

# Adding lecturers
print(university.lecturers(1, "Dr. Kasozi", "Computer Science"))
print(university.lecturers(2, "Rev. Footi", "Data Science"))

# Retrieve all data
print("\nStudents:", university.get_students())
print("Courses:", university.get_courses())
print("Lecturers:", university.get_lecturers())

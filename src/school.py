class Person(object):
    def __init__(self, name: str) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Student(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class TooManyStudents(Exception):
    pass

class Classroom(object):
    def __init__(self, teacher: Teacher, students: list[Student], course_title: str) -> None:
        self.teacher = teacher
        self.students = students
        self.course_title = course_title
    
    def add_student(self, student: Student) -> None:
        if len(self.students) > 10:
            raise TooManyStudents
        self.students.append(student)
    
    def remove_student(self, student_name: str) -> None:
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
    
    def change_teacher(self, teacher: Teacher):
        self.teacher = teacher


import pytest
from src.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def sample_teacher():
    return Teacher(name="Professor X")


@pytest.fixture
def sample_student():
    return Student(name="Gene Grey")


@pytest.fixture
def sample_classroom(sample_teacher, sample_student):
    student_list = ["Bob", "Alice", "Eve"]
    initial_students = [Student(student) for student in student_list]
    return Classroom(
        teacher=sample_teacher, students=initial_students, course_title="Dark Arts"
    )


def test_add_student(sample_classroom, sample_student):
    # Test adding a student to the classroom
    initial_student_count = len(sample_classroom.students)
    sample_classroom.add_student(sample_student)
    assert len(sample_classroom.students) == initial_student_count + 1


def test_add_student_raises_exception(sample_classroom, sample_student):
    # Test that TooManyStudentException is raised when adding more than 10 students
    with pytest.raises(TooManyStudents):
        for _ in range(10):
            sample_classroom.add_student(sample_student)


def test_remove_student(sample_classroom, sample_student):
    # Test removing a student from the classroom
    sample_classroom.remove_student(sample_student.name)
    assert sample_student not in sample_classroom.students


def test_change_teacher(sample_classroom, sample_teacher):
    # Test changing the teacher of the classroom
    initial_teacher = sample_classroom.teacher
    sample_classroom.change_teacher(Teacher("Professor Y"))
    # assert sample_classroom.teacher == sample_teacher
    assert sample_classroom.teacher != initial_teacher

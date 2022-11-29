from django.test import TestCase
from CS361_Project.models import Supervisor


class test_DeleteCourse(TestCase):

    def setUp(self):
        self.supervisor = Supervisor()

    def test_TooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.supervisor.deleteCourse("CompSci", 150, "Survey of Computer Science")

    def test_TooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.supervisor.deleteCourse("CompSci")

    def test_WrongDepartmentType(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Department should be a string"):
            self.supervisor.deleteCourse(25, 150)

    def test_WrongCourseNumType(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Course number should be an integer"):
            self.supervisor.deleteCourse("CompSci", "150")

    def test_NoParameters(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="There are no parameters"):
            self.supervisor.deleteCourse()

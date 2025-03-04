from django.db import models


class Account(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)


class Supervisor(models.Model):
    id = models.OneToOneField("Account", primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)

    def createCourse(self, department, courseNum, courseName):
        pass

    def deleteCourse(self, department, courseNum):
        pass

    def editCourse(self, department, courseNum):
        pass


class Instructor(models.Model):
    id = models.OneToOneField("Account", primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)


class TA(models.Model):
    id = models.OneToOneField("Account", primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)


class Course(object):

    def init(self, department, courseNum, name):
        self.department = department
        self.courseNum = courseNum
        self.name = name

    def str(self):
        pass

    def setName(self, name):
        pass

    def getName(self):
        pass

    def setCourseNum(self, courseNum):
        pass

    def getCourseNum(self):
        pass

    def getDepartment(self):
        pass

    def setDepartment(self, department):
        pass
        
    def editCourse(self, department, courseNum):
        pass


class Course(object):

    def __init__(self, department, courseNum, name):
        self.department = department
        self.courseNum = courseNum
        self.name = name

    def __str__(self):
        pass

    def setName(self, name):
        pass

    def getName(self):
        pass

    def setCourseNum(self, courseNum):
        pass

    def getCourseNum(self):
        pass

    def getDepartment(self):
        pass

    def setDepartment(self, department):
        pass

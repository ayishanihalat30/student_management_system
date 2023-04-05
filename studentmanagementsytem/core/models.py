from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


class Department(models.Model):
    department = models.CharField(max_length=75)

    def __str__(self):
        return self.department





class Semester(models.Model):
    semester = models.CharField(max_length=1)

    def __str__(self):
        return self.semester
class Academic_year(models.Model):
    academic=models.CharField(max_length=4)

    def __str__(self):
        return str(self.academic)

class Subject_model(models.Model):
    subject_name = models.CharField(max_length=75)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    Registrations_No = models.IntegerField(null=True)
    Branch = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, null=True)
    semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=13, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
class Subject_code(models.Model):
    subject_code = models.CharField(max_length=10,null=True)

    def __str__(self):
        return str(self.subject_code)


class Allotted_Subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject_model, null=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)
    academic = models.ForeignKey(Academic_year, null=True, on_delete=models.CASCADE)

    subject_code= models.ForeignKey(Subject_code, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.subject) + " - " + str(self.semester)

class details(models.Model):
    student_name=models.CharField(null=True,max_length=30)
    Subject1=models.CharField(null=True,max_length=30)
    Subject2= models.CharField(null=True,max_length=30)
    Subject3=models.CharField(null=True,max_length=30)
    mark1=models.IntegerField(null=True)
    mark2= models.IntegerField(null=True)
    mark3= models.IntegerField(null=True)
    attendence=models.CharField(null=True,max_length=30)
    assignment1=models.CharField(null=True,max_length=500)
    assignment2 = models.CharField(null=True,max_length=500)
    assignment3 = models.CharField(null=True,max_length=500)
    # notes=models.FileField(upload_to='adminapp/document',null=True)
    def __str__(self):
        return str(self.mark1)



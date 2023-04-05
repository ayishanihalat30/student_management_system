from core.models import Allotted_Subject,Academic_year, Student, Teacher, Subject_code,Department, Semester, Subject_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'Registrations_No', 'Branch', 'phone', 'semester']
class SubjectCode(ModelForm):
    class Meta:
        model=Subject_code
        fields=['subject_code']

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'phone']

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department']

class semesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = ['semester']


class SubjectForm(ModelForm):
    class Meta:
        model = Subject_model
        fields = ['subject_name']
class AcademicForm(ModelForm):
    class Meta:
        model = Academic_year
        fields = ['academic']

class AllotedSubjectForm(forms.ModelForm):
    class Meta:
        model = Allotted_Subject
        fields = ['teacher','subject','department','semester','academic','subject_code']



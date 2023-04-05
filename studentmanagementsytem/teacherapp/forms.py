from core.models import  Allotted_Subject,Academic_year,Semester,Student,details
from django.forms import ModelForm
from django import forms


class AcademicForm(ModelForm):
    class Meta:
        model = Academic_year
        fields = ['academic']
class semesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = ['semester']


class Studdetails(ModelForm):
    class Meta:
        model=details
        fields=['student_name','Subject1','Subject2','Subject3','mark1','mark2','mark3','attendence','assignment1','assignment2','assignment3']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'Registrations_No', 'Branch', 'phone', 'semester']

class AllotedSubjectForm(forms.ModelForm):
    class Meta:
        model = Allotted_Subject
        fields = ['teacher','subject','department','semester','subject_code','academic']
class Text(forms.Form):
    TextField=forms.CharField(widget=forms.Textarea)
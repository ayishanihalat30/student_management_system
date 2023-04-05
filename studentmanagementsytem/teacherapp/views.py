from core.models import *
from django.shortcuts import render, redirect
from .forms import AcademicForm,semesterForm,Studdetails,StudentForm
from django.contrib.auth.models import User
import os


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'teacherapp/index.html')


def personal_details(request):
    g = User.objects.all().order_by('-last_login')[0]
    print(g)
    subjects = Allotted_Subject.objects.all()
    for i in subjects:
        print(i)
    context = {
        'subjects': subjects,
    }
    return render(request, 'teacherapp/subject_list.html', context)

def add_year(request):
    form = AcademicForm()
    academic = Academic_year.objects.all()
    if request.method == 'POST':
        form = AcademicForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('semester'))

    context = {
        'form': form,
        'academic': academic,
    }
    return render(request, 'teacherapp/add_academic year.html', context)

def select(request):

    return render(request, 'teacherapp/select academic year,semester.html')

def subject(request):
    allots = Allotted_Subject.objects.all()
    for i in allots:
        print(i)

    context = {
        'allots': allots,

    }

    return render(request, 'teacherapp/subject.html', context)

# def select_subject(request,subject):
#     allots = Allotted_Subject.objects.all()
# 
#     for i in allots:
#         print(i.subject)
#     return render(request,'teacherapp/coursediary.html')


def mark(request):
    form = Studdetails()
    mark = details.objects.all()
    if request.method == 'POST':
        form = Studdetails(request.POST)
        if form.is_valid():
            print("Form is valid")

            student_name = form.cleaned_data['student_name']
            Subject1 = form.cleaned_data['Subject1']
            Subject2 = form.cleaned_data['Subject2']
            Subject3 = form.cleaned_data['Subject3']
            mark1 = form.cleaned_data['mark1']
            mark2 = form.cleaned_data['mark2']
            mark3 = form.cleaned_data['mark3']
            attendence = form.cleaned_data['attendence']
            assignment1 = form.cleaned_data['assignment1']
            assignment2 = form.cleaned_data['assignment2']
            assignment3 = form.cleaned_data['assignment3']
            # notes = form.cleaned_data['notes']

            marks= details( student_name=student_name, Subject1=Subject1, Subject2=Subject2,Subject3=Subject3,mark1=mark1,mark2=mark2,mark3=mark3,attendence=attendence, assignment1=assignment1,assignment2=assignment2,assignment3=assignment3,
                       )
            marks.save()
            # print(mark)
            messages.success(request, 'Approved for ' + student_name)
            # return redirect('admin-home')

    context = {

        'mark': mark,
        'form': form,
    }
    return render(request, 'teacherapp/add_details.html', context)


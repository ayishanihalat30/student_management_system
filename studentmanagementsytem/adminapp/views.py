from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from core.models import *
from core.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from collections import defaultdict
# from gensim import corpora
# from gensim import models
# from gensim import similarities


# Create your views here.
def home(request):
    return render(request, 'adminapp/index.html')


def adminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    login_str = 'logout'
    context = {'login': login_str}
    return render(request, 'adminapp/login.html', context)


def add_department(request):
    form = DepartmentForm()
    departments = Department.objects.all()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('department'))
            return redirect('admin-home')
    context = {
        'form': form,
        'departments': departments,
    }
    return render(request, 'adminapp/add_department.html', context)





def add_semester(request):
    form = semesterForm()
    semesters = Semester.objects.all()
    if request.method == 'POST':
        form = semesterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('semester'))
            return redirect('admin-home')
    context = {
        'form': form,
        'semesters': semesters,
    }
    return render(request, 'adminapp/add_semester.html', context)

def add_academic(request):
    form = AcademicForm()
    academic = Academic_year.objects.all()
    if request.method == 'POST':
        form = AcademicForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('academic'))
            return redirect('admin-home')
    context = {
        'form': form,
        'academic_year': academic,
    }
    return render(request, 'adminapp/add_academic year.html', context)


def add_subject_code(request):
    form = SubjectCode()
    subject_code = Subject_code.objects.all()
    if request.method == 'POST':
        form = SubjectCode(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('subjectcode'))
            return redirect('admin-home')
    context = {
        'form': form,
        'subject_codes': subject_code,
    }
    return render(request, 'adminapp/add_division.html', context)
def add_subject(request):
    form = SubjectForm()
    subject_names = Subject_model.objects.all()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('subject_name'))
            return redirect('admin-home')
    context = {
        'form': form,
        'subjects': subject_names,
    }
    return render(request, 'adminapp/add_subject.html', context)


def add_teacher(request):
    form = CreateUserForm()
    form2 = TeacherForm()
    facultys = Teacher.objects.all()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = TeacherForm(request.POST)
        if form.is_valid() and form2.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            g = User.objects.create_user(username=username, email=email, password=password1, is_staff=True)
            g.save()
            person = User.objects.all().last()
            print(person)
            first_name = form2.cleaned_data['first_name']
            last_name = form2.cleaned_data['last_name']
            phone = form2.cleaned_data['phone']
            g = Teacher(user=person, first_name=first_name, last_name=last_name, phone=phone)
            g.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('admin-home')
    page = 'Teacher Registration'
    context = {
        'form': form,
        'form2': form2,
        'page': page,
        'faculty': facultys,
    }
    return render(request, 'adminapp/add_teacher.html', context)


def add_student(request):
    form = CreateUserForm()
    form2 = StudentForm()
    students = Student.objects.all()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = StudentForm(request.POST)
        if form.is_valid() and form2.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            g = User.objects.create_user(username=username, email=email, password=password1, is_staff=False)
            g.save()
            person = User.objects.all().last()
            print(person)
            name = form2.cleaned_data['name']
            Registrations_No = form2.cleaned_data['Registrations_No']
            Branch = form2.cleaned_data['Branch']
            phone = form2.cleaned_data['phone']
            semester = form2.cleaned_data['semester']

            g = Student(user=person, name=name, Registrations_No=Registrations_No, Branch=Branch, phone=phone,
                        semester=semester)
            g.save()
            print(g)
            messages.success(request, 'Account was created for ' + username)
            return redirect('admin-home')
    page = 'Student Registration'
    context = {
        'form': form,
        'form2': form2,
        'page': page,
        'students': students,
    }
    return render(request, 'adminapp/add_student.html', context)


# def student_teacher(request):
#     form = CreateUserForm()
#     form2 = TeacherForm()
#     facultys = Teacher.objects.all()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         form2 = TeacherForm(request.POST)
#         if form.is_valid() and form2.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password1 = form.cleaned_data['password1']
#             password2 = form.cleaned_data['password2']
#             g = User(username=username, email=email, password=password1, is_staff=True)
#             g.save()
#             person = User.objects.all().last()
#             print(person)
#             first_name = form2.cleaned_data['first_name']
#             last_name = form2.cleaned_data['last_name']
#             phone = form2.cleaned_data['phone']
#             g = Teacher(user=person, first_name=first_name, last_name=last_name, phone=phone)
#             g.save()
#             messages.success(request, 'Account was created for ' + username)
#             return redirect('admin-home')
#     page = 'Teacher Registration'
#     context = {
#         'form': form,
#         'form2': form2,
#         'page': page,
#         'faculty': facultys,
#     }
#     return render(request, 'adminapp/add_teacher.html', context)


def teacher_subject_assign(request):
    form = AllotedSubjectForm()
    if request.method == 'POST':
        form = AllotedSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            '''teacher = form.cleaned_data['teacher']
            subject = form.cleaned_data['subject']
            department = form.cleaned_data['department']
            semester = form.cleaned_data['semester']
            division = form.cleaned_data['division']
            g = Allotted_Subject(teacher=teacher,subject=subject,department=department,semester=semester,division=division)
            g.save'''
            allots = Allotted_Subject.objects.all()
            context = {
                'allots': allots,
            }
            messages.success(request, 'Subject assigned successfully')

            return render(request, 'adminapp/alloted_subjects.html', context)
    context = {
        'form': form,
    }
    return render(request, 'adminapp/teacher_subject_assign.html', context)


def alloted_subjects(request):
    allots = Allotted_Subject.objects.all()
    context = {
        'allots': allots,
    }

    return render(request, 'adminapp/alloted_subjects.html', context)


def teacher_subject_list(request, n):
    teacher = Allotted_Subject.objects.get(id=n)
    subjects = teacher.subject_set.all()
    form = SubjectForm()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.teacher = teacher
            obj.save()
            messages.success(request, 'Subject assigned successfully')

            allots = Allotted_Subject.objects.all()
            context = {
                'allots': allots,
            }

            return render(request, 'adminapp/alloted_subjects.html', context)
    context = {
        'subjects': subjects,
        'form': form,
    }
    return render(request, 'adminapp/teacher_subject_list.html', context)

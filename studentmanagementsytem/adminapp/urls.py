from core.views import home
from django.urls import path 
from .views import *

urlpatterns = [
    path('admin-login/', adminLogin , name='admin-login'),
    path('', home , name='admin-home'),
    path('add_department/',add_department,name='add_department'),
    path('add_semester/',add_semester,name='add_semester'),
    path('add_subject/',add_subject,name='add_subject'),
    path('add_subject_code/',add_subject_code,name='add_subject_code'),
    path('add_teacher/',add_teacher,name='add_teacher'),
    path('add_student/',add_student,name='add_student'),
    path('add_academic/', add_academic, name='add_academic'),
    path('teacher-subject-assign/', teacher_subject_assign, name='teacher-subject-assign'),
    path('alloted_subjects/',alloted_subjects,name='alloted_subjects'),
    path('teacher-subject-list/<str:n>/', teacher_subject_list, name='teacher-subject-list'),

]

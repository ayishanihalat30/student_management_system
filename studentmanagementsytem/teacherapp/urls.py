from django.urls import path 
from .views import *
#anser_paper_list
urlpatterns = [
    path('', home , name='teacher-home'),
    path('personal_details/', personal_details , name='teacher-personal_details'),
    path('add_year/',add_year,name ='add_year'),
    path('select/',select,name='select'),
    path('subject/',subject,name='subject'),
    path('mark/', mark, name='mark'),
# path('select_subject/<str:subject>',select_subject, name='subject'),
]   

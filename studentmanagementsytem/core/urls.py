from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home , name='home' ),
    path('login/', loginpage ,name='login'),
path('StudentLogin/', StudentLogin ,name='StudentLogin'),
path('register/', register ,name='register'),
path('det/', det ,name='det'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
'''
    
    path('studentRegister/', studentRegister ,name='studentRegister'),
    path('teacherRegister/', teacherRegister ,name='teacherRegister'),    '''

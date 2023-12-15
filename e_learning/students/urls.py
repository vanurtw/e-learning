from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterStudent.as_view(), name='register_student'),


]
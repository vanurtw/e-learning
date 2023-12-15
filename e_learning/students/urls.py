from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterStudent.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),

]

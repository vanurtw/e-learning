from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterStudent.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', StudentCourseList.as_view(), name='student_course_list'),
    path('course/<pk>/', StudentCourseDetail.as_view(), name='student_course_detail'),
    path('course/<pk>/<module_id>/', StudentCourseDetail.as_view(), name='student_course_detail_module'),

]

from django.urls import path
from . import view


urlpatterns = [
    path('subjects/', view.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', view.SubjectDetailView.as_view(), name='subject_detail'),
    path('courses/<int:pk>/enroll/', view.CourseEnrollView.as_view(), name='course_enroll')

]

from django.urls import path, include
from . import view
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', view.ViewSetCourse)


urlpatterns = [
    path('subjects/', view.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', view.SubjectDetailView.as_view(), name='subject_detail'),
    path('', include(router.urls)),

]

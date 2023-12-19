from django.urls import path
from . import views


urlpatterns = [
    path('room/<int:course_id>/', views.course_chat_room, name='course_chat_room'),
]
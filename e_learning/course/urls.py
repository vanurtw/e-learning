from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='course/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='course/logout.html'), name='logout'),
    path('course/', views.CourseList.as_view(), name='manage_course_list'),
    path('course/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('course/update/<int:pk>/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('course/delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('<int:pk>/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('content/<int:id>/delete/', views.ContentDelete.as_view(), name='module_content_delete'),
    path('module/<int:id>/', views.ModuleContentListView.as_view(), name='module_content_list'),


]

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='course/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='course/logout.html'), name='logout')

]

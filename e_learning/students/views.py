from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate


# Create your views here.


class RegisterStudent(CreateView):
    template_name = 'students/register.html'
    success_url = reverse_lazy('student_course_list')
    form_class = UserCreationForm

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        login(self.request, user)
        return result

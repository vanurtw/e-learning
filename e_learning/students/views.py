from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView
from django.contrib.auth import login, authenticate
from .forms import CourseEnrollForm
from django.contrib.auth.mixins import LoginRequiredMixin
from course.models import Course


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


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])


class StudentCourseList(LoginRequiredMixin, ListView):
    template_name = 'students/list.html'
    model = Course

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetail(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = course.module_created.get(id=self.kwargs['module_id'])
        else:
            context['module'] = course.module_created.all()[0]
        return context

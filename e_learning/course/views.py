from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Course
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# Create your views here.

class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerMixin):
    model = Course
    fields = ['title', 'owner', 'subject', 'created']
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'course/form.html'


class CourseList(OwnerCourseMixin, ListView):
    template_name = 'course/course_list.html'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    pass


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'course/delete.html'

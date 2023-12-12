from django.forms.models import inlineformset_factory
from .models import Course, Module, Subject

ModuleFormSet = inlineformset_factory(Course, Module, fields=['title', 'description'], extra=2, can_delete=True)

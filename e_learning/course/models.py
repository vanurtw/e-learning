from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string

from .fields import OrderFields


# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    students = models.ManyToManyField(User, related_name='courses_joined', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, related_name='module_created', on_delete=models.CASCADE)
    order = OrderFields(blank=True, for_fields=['course'])
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title}. {self.title}'


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': (
                                         'text',
                                         'video',
                                         'image',
                                         'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderFields(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class BaseContent(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='%(class)s_related')
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def render(self):
        return render_to_string(f'content/{self._meta.model_name}.html', {'item': self})

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(BaseContent):
    content = models.TextField()


class File(BaseContent):
    file = models.FileField(upload_to='files/')


class Image(BaseContent):
    file = models.ImageField(upload_to='image/')


class Video(BaseContent):
    video = models.URLField()

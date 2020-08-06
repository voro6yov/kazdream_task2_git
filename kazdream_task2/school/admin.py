from django.contrib import admin

from .models import Teacher, Lesson, Pupil

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Pupil)

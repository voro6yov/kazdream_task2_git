from django.views import generic

from .models import Lesson


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'lessons'

    def get_queryset(self):
        return Lesson.objects.all()

from django.views import generic

from .models import Lesson


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'lesson'

    def get_queryset(self):
        return Lesson.objects.get()

from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    


class Lesson(models.Model):
    title = models.CharField(max_length=60)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.title
    


class Pupil(models.Model):
    name = models.CharField(max_length=60)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
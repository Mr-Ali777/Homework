from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(blank=True, verbose_name="Описание")
    duration = models.DurationField(verbose_name="Продолжительность")

    def __str__(self):
        return f"{self.pk} - {self.title}"


class Topic(models.Model):
    topic_name = models.CharField(max_length=100, verbose_name="Название темы")
    description = models.TextField(blank=True, verbose_name="Описание темы")
    duration = models.DurationField(verbose_name="Продолжительность изучения темы")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pk} - {self.topic_name}"


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    course_author = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.last_name}"




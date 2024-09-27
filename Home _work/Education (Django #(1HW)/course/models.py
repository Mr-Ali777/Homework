from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название курса")
    duration = models.CharField(max_length=50, verbose_name="Продолжиьтельность курса")
    description = models.TextField(verbose_name="Описание курса")

    def __str__(self):
        return f'{self.pk} - {self.title}'

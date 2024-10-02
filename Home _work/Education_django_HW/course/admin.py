from django.contrib import admin
from .models import Course, Topic, Author


admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Author)
# Generated by Django 5.1.1 on 2024-10-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_add_model_Topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('course_author', models.ManyToManyField(to='course.course')),
            ],
        ),
    ]
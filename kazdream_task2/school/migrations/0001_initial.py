# Generated by Django 3.1 on 2020-08-06 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('title', models.CharField(max_length=60)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='school.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.lesson')),
            ],
        ),
    ]

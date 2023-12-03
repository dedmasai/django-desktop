# Generated by Django 4.2.7 on 2023-11-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskN', models.IntegerField(default=0)),
                ('userN', models.IntegerField(default=0)),
                ('numbInV', models.IntegerField(default=0)),
                ('uAnswer', models.IntegerField(default=0)),
                ('correct', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varNumber', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('text', models.TextField(blank=True)),
                ('answer', models.IntegerField(default=0)),
                ('rightAnswCount', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

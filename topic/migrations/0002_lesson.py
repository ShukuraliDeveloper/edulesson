# Generated by Django 4.0.2 on 2022-02-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Mavzu')),
                ('description', models.TextField(verbose_name='Maruza')),
                ('photo', models.ImageField(upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
# Generated by Django 4.0.2 on 2022-02-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0009_post_photo_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(),
        ),
    ]
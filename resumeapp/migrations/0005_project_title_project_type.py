# Generated by Django 4.2.7 on 2023-12-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_projectour_remove_project_nmadir_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

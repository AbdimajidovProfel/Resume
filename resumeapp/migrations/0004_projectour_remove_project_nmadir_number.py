# Generated by Django 4.2.7 on 2023-12-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0003_remove_skills_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectOur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('nmadir_number', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='nmadir_number',
        ),
    ]
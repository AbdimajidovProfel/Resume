from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avas/', blank=True, null=True, verbose_name="Avatar")
    bio = models.TextField(verbose_name='Bio', blank=True, null=True)


class About(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=55, verbose_name="Name")
    date_birth = models.CharField(max_length=111)
    adress = models.TextField(verbose_name='Adress')
    zip_code = models.IntegerField(verbose_name='Zip code')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=66, verbose_name='Phone')
    project_number = models.IntegerField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    educations = models.ForeignKey('Education', on_delete=models.CASCADE)
    experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
    skills = models.ForeignKey('Skills', on_delete=models.CASCADE)
    awards = models.ForeignKey('Awards', on_delete=models.CASCADE)

    def __str__(self):
        return self.educations


class Education(models.Model):
    title = models.CharField(max_length=255)
    unv_name = models.CharField(max_length=150)
    content = models.TextField(verbose_name='Content')
    year = models.CharField(max_length=111)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    unv_name = models.CharField(max_length=150)
    content = models.TextField(verbose_name='Content')
    year = models.CharField(max_length=111)

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=250)
    prosent = models.IntegerField()
    l_week_prosent = models.IntegerField()
    l_month_prosent = models.IntegerField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=99)
    prosent = models.IntegerField()

    def __str__(self):
        return self.title


class Awards(models.Model):
    title = models.CharField(max_length=255)
    unv_name = models.CharField(max_length=150)
    content = models.TextField(verbose_name='Content')
    year = models.CharField(max_length=111)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=266, verbose_name='Title')
    content = models.TextField(verbose_name='Content')

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    image = models.ImageField()

    def __str__(self):
        return self.title


class ProjectOur(models.Model):
    title = models.CharField(max_length=222)
    nmadir_number = models.IntegerField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=266)
    content = models.TextField(verbose_name='Content')
    message = models.ManyToManyField("Message", verbose_name='Message', blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creared')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.title


class Message(models.Model):
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:20]


class Contact(models.Model):
    f_name = models.CharField(max_length=55, verbose_name='Your Name')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=255, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-id']



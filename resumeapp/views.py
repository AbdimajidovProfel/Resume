from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .models import *
from .forms import *


def indexView(request):
    about = About.objects.all()
    rsm = Resume.objects.all()
    edu = Education.objects.all()
    exp = Experience.objects.all()
    skls = Skills.objects.all()
    skl = Skill.objects.all()
    Pour = ProjectOur.objects.all()
    awr = Awards.objects.all()
    srv = Services.objects.all()
    pr = Project.objects.all()
    blg = Blog.objects.all()
    form = ContactForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {"form": form,
               'about': about,
               'rsm': rsm,
               'edu': edu,
               'exp': exp,
               'skils': skls,
               'awards': awr,
               'services': srv,
               'project': pr,
               'blogs': blg,
               'Pour': Pour,
               'skl': skl,
               }
    return render(request, 'index.html', context)


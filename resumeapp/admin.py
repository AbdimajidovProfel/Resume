from django.contrib import admin
from .models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['f_name', 'email', 'created']
    list_display_links = ['f_name', 'email']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    list_display_links = ['name', 'phone']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_display_links = ['title']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_display_links = ['title']


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(ProjectOur)
class ProjectOurAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_display_links = ['title']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_display_links = ['title']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_display_links = ['title']


admin.site.register(Project)

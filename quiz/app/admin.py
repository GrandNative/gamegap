from django.contrib import admin
from . import models


@admin.register(models.Question)
class EventPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.Answer)
class EventPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "question")


@admin.register(models.UserRate)
class EventPartAdmin(admin.ModelAdmin):
    list_display = ('id', "question", 'user')
# Register your models here.

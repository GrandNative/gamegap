from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    active = models.BooleanField(null=True, blank=True)
    is_start = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserRate(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    is_true = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True, null=True)
    is_true = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class ConvertBackupDownloadItem(models.Model):
#     gener_link = models.CharField(max_length=150, blank=True, null=True)
#     gener_mirror_link = models.CharField(max_length=150, blank=True, null=True)
#     mirror_short_link = models.CharField(max_length=150, blank=True, null=True)
#     short_link = models.CharField(max_length=150, blank=True, null=True)
#     size = models.IntegerField(blank=True, null=True)
#     counter = models.IntegerField(blank=True, null=True)
#     cost = models.IntegerField(blank=True, null=True)
#     down_parent_id = models.IntegerField(blank=True, null=True)
#     video_id = models.IntegerField(blank=True, null=True)
#     is_all = models.BooleanField(blank=True, null=True)
#     publish_time = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from portfolios.models import Portfolio, Tech
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    tech_category = models.ManyToManyField(
        Tech,
        related_name='user_category',
        blank=True
    )
    nickname = models.TextField(blank=True)
    profile_img = models.TextField(null=True, blank=True)
    verified_img = models.TextField(null=True, blank=True)
    company = models.TextField(default='no', blank=True)
    address = models.TextField(blank=True)
    sns_id = models.TextField(blank=True)
    auth = models.IntegerField(null=True)
    major = models.TextField(blank=True)
    confirmed = models.BooleanField(default=False)
    grade = models.IntegerField(null=True)
    language = models.TextField(blank=True)
    introduce = models.TextField(blank=True)
    secession = models.BooleanField(default=False)
    award_1 = models.TextField(blank=True)
    award_2 = models.TextField(blank=True)
    award_3 = models.TextField(blank=True)
    

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="message_receiver", on_delete=models.CASCADE)
    sentAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=150)
    isRead = models.BooleanField(default=False)
    # objects = models.Manager()


# class 
#     fields = ('id', 'email', 'password1', 'password2', 'name', 'grade', 'company', 'tech', 'confirm_img',)

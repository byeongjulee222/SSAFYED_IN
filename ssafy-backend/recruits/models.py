from django.db import models
from django.conf import settings
from portfolios.models import Tech
# Create your models here.
class Recruit(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user 는 N:M
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='recruit', on_delete=models.CASCADE)
    applicant_user = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name='apllicant_company',
        blank=True)
    title = models.TextField()
    end_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    region = models.TextField(blank=True)
    qualitificatioin = models.TextField(blank=True)
    condition = models.TextField(blank=True)
    tech_category = models.ManyToManyField(
        Tech, 
        related_name='recruit_category',
        blank=True)
    content = models.TextField(blank=True)
    population = models.TextField(blank=True)
    complete = models.BooleanField(default=False) # 채용 끝남을 체크
    company_url = models.TextField(blank=True)
    recruit_logo = models.TextField(blank=True)
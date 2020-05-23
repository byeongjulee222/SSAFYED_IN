from django.db import models
from django.conf import settings
from portfolios.models import Tech
# Create your models here.

class Competition(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='competition',on_delete=models.CASCADE)
    applicant_competition_user = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name='applicant_competition_company',
        blank=True)
    title = models.TextField()
    end_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    region = models.TextField(blank=True)
    qualitification = models.TextField(blank=True)
    # condition = models.TextField()
    tech_category = models.ManyToManyField(
        Tech, 
        related_name='competiton_category',
        blank=True)
    content = models.TextField(blank=True)
    population = models.TextField(blank=True)
    complete = models.BooleanField(default=False) # 채용 끝남을 체크
    company_url = models.TextField(blank=True)
    # recruit_logo = models.ImageField(null=True, blank=True)
    recruit_logo = models.TextField(blank=True)




# class CompetitionsCompetition(models.Model):
#     title = models.TextField()
#     end_date = models.DateField()
#     created_at = models.DateField()
#     update_at = models.DateField()
#     region = models.TextField()
#     qualitificatioin = models.TextField()
#     content = models.TextField()
#     population = models.TextField()
#     complete = models.IntegerField()
#     company_url = models.TextField()
#     recruit_logo = models.CharField(max_length=100)
#     user_name = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'competitions_competition'


# class CompetitionsCompetitionApplicantCompetitionUser(models.Model):
#     competition = models.ForeignKey(CompetitionsCompetition, models.DO_NOTHING)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'competitions_competition_applicant_competition_user'
#         unique_together = (('competition', 'user'),)


# class CompetitionsCompetitionTechCategory(models.Model):
#     competition = models.ForeignKey(CompetitionsCompetition, models.DO_NOTHING)
#     tech = models.ForeignKey(PortfoliosTech, models.DO_NOTHING)

    # class Meta:
    #     managed = False
    #     db_table = 'competitions_competition_tech_category'
    #     unique_together = (('competition', 'tech'),)
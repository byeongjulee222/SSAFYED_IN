from django.db import models
from django.conf import settings

# Create your models here.
class Tech(models.Model):
    tech_stack = models.TextField()
    def __str__(self):
        return self.tech_stack


class Portfolio(models.Model):
    title = models.TextField()
    tech_category = models.ManyToManyField(
        Tech,
        related_name='portfolio_category',
        blank=True
    )  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    public = models.BooleanField(default=True) #공개 비공개
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    project_start = models.DateField(auto_now=True)
    project_end = models.DateField(auto_now=True)
    content_img_1 = models.TextField(blank=True)
    content_sub_1 = models.TextField(blank=True)
    content_img_2 = models.TextField(blank=True)
    content_sub_2 = models.TextField(blank=True)
    content_img_3 = models.TextField(blank=True)
    content_sub_3 = models.TextField(blank=True)
    content_img_4 = models.TextField(blank=True)
    content_sub_4 = models.TextField(blank=True)
    content_img_5 = models.TextField(blank=True)
    content_sub_5 = models.TextField(blank=True)
    content_img_6 = models.TextField(blank=True)
    content_sub_6 = models.TextField(blank=True)
    content_img_7 = models.TextField(blank=True)
    content_sub_7 = models.TextField(blank=True)
    content_img_8 = models.TextField(blank=True)
    content_sub_8 = models.TextField(blank=True)
    content_img_9 = models.TextField(blank=True)
    content_sub_9 = models.TextField(blank=True)
    content_img_10 = models.TextField(blank=True)
    content_sub_10 = models.TextField(blank=True)


class Comment(models.Model):
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
# contents 의 필드는 아직 테이블로 해야하는지 모르겠음
    
# content 지우고  img를 제한해서 max 10개. 
# class Content(models.Model):
    # portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


# class PortfoliosTech(models.Model):
#     tech_stack = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'portfolios_tech'


# class PortfoliosContent(models.Model):
#     content_img = models.TextField()
#     content_sub = models.TextField()
#     portfolio = models.ForeignKey('PortfoliosPortfolio', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'portfolios_content'


# class PortfoliosPortfolio(models.Model):
#     title = models.TextField()
#     public = models.IntegerField()
#     created_at = models.DateField()
#     update_at = models.DateField()
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'portfolios_portfolio'


# class PortfoliosPortfolioTechCategory(models.Model):
#     portfolio = models.ForeignKey(PortfoliosPortfolio, models.DO_NOTHING)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'portfolios_portfolio_tech_category'
#         unique_together = (('portfolio', 'user'),)


from django.urls import path
from . import views

urlpatterns = [
    path('recruits/', views.recruit_list),
    path('recruits/<int:recruit_pk>/', views.recruit_detail),
    path('recruits/<int:recruit_pk>/update/', views.recruit_delete_update),
    path('recruits/<int:recruit_pk>/applicant/', views.recruit_applicant),
    path('recruits/<int:recruit_pk>/sendmail/', views.recruit_send_mail),
    path('recruits/create/', views.recruit_create),
    
]
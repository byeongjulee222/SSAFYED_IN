from django.urls import path
from . import views


urlpatterns = [
    path('competitions/', views.competition_list ),
    path('competitions/pagelist/', views.competiton_page ),
    path('competitions/create/', views.competition_create ),
    path('competitions/<int:competition_pk>/', views.competition_detail ),
    path('competitions/<int:competition_pk>/update/', views.competition_delete_update ),
    path('competitions/<int:competition_pk>/applicant/', views.competition_applicant ),
    path('competitions/<int:competition_pk>/sendmail/', views.competition_send_mail ),
]
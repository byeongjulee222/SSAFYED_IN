from django.urls import path
from . import views

urlpatterns = [
    path('portfolios/', views.portfolio_list ),
    path('portfolios/pagelist/', views.portfolio_page ),
    path('portfolios/create/', views.portfolio_create ),
    path('portfolios/<int:portfolio_pk>/', views.portfolio_detail ),
    path('portfolios/<int:portfolio_pk>/delete_update/', views.portfolio_delete_update ),
    path('portfolios/<int:portfolio_pk>/comment/', views.comment_create),
    path('portfolios/<int:portfolio_pk>/comment/<int:comment_pk>/', views.comment_update_delete),
    path('techs/', views.tech),
]
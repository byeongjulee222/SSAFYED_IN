from django.urls import path, include
from . import views

urlpatterns = [
    path('accouts/<int:id>/', views.user_detail),
    path('accouts/', views.user_name),
    path('accouts/authenticate/', views.user_authenticate),
    path('accouts/signup/', views.user_signup),
    path('accouts/login/', views.login),
    path('accouts/logout/', views.logout),
    path('accouts/update/<int:id>/', views.user_update),
    path('accouts/password/<int:id>/', views.password_update),
    path('accouts/password_email/', views.password_send_mail),
    path('accouts/sendmessage/<int:re_id>/', views.send_message),
    path('accouts/message_list/<int:id>/', views.list_message),
    path('accouts/message_read/<int:message_id>/', views.read_message),
    path('accouts/user_page/', views.user_page),
    path('accouts/tech_page/', views.tech_page),
    # path('accouts/signup/', views.signup),
    # path('', views.UserListView.as_view()),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

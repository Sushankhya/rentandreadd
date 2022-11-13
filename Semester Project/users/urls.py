from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerUser, name = 'register'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset.html"),name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/newpassword_done.html"),name='password_reset_complete'),


    path('', views.profiles, name='profile')
]
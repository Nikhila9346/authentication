from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]


'''
Session based - way to store info about user whether the user on the server(session storage) is logged in or not

Cookies - stores the activities
'''
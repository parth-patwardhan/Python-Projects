from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_request, name='login_auth'),
    path('register', views.register_request, name='register_page'),
    path('logout', views.logout_request, name='logout'),
]
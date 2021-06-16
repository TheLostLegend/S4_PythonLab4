from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/', views.page, name='userPage'),
    path('delete/', views.deleteTask, name='delete'),
]

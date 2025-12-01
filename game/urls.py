from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # root URL → home/index page
    path('play/', views.game, name='game'),  # /play/ URL → game page
]

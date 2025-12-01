from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),     # first page
    path('play/', views.index, name='game'),  # game page
]

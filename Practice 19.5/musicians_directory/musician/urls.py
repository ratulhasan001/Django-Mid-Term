from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_musician, name = 'add_musician'),
]
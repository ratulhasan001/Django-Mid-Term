from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('details/<int:id>/', views.DetailCarView.as_view(), name='car_details'),
    path("buy_car/<int:id>/", views.update_quantity , name="buy_car"),
]

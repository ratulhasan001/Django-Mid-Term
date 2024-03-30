from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('', views.home, name="homepage"),
]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',include('app.urls')),
]

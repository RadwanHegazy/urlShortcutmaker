from django.urls import path
from . import views


urlpatterns = [
    path('',views.user_details,name='details'),
    path('gethashBylink/',views.get_hash_by_link,name='getCode'),
]
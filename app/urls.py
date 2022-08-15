from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home,name='home'),

    # auth
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

    path('<str:hash>/',views.open,name='open'),
]
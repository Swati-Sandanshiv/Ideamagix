from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('handleLogin',views.handleLogin,name='handleLogin'),
    # path('lecture',views.lecture,name='lecture'),
    path('logout',views.logout,name='logout'),
]
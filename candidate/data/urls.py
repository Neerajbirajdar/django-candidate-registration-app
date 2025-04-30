from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
from dj_rest_auth.registration.views import RegisterView

urlpatterns=[
    path("register/",RegisterView.as_view(), name="rest_register"),
    path('login/',auth_view.LoginView.as_view(), name="login"),
    path('logout/',auth_view.LogoutView.as_view(), name="logout"),
    path('add/',add,name="add"),
    path('update/',update,name="update"),
    path('getall/',get_all,name="get all"),
    path('get/<int:x>',get,name="get"),
    path('delete/',delete,name="delete")
]
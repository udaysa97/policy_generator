from django.urls import path

from logics import views


urlpatterns = [
    path('login', views.Login.as_view(), name="loginAPI"),
    path('accept_policies', views.AcceptPolicy.as_view(), name="poiciesAPI"),
    path('custom_notifications', views.CustomPolicyGenerate.as_view(), name="poiciesAPI")
]

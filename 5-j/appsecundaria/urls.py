from django.urls import path,include
from appsecundaria import views

urlpatterns = [
    path("",views.index_vista,name="index_vista"),
]

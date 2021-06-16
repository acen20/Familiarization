from django.urls import path
from . import views
#adding urls

urlpatterns = [
    path('', views.index, name = "index")
]

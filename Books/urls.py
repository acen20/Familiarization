from django.urls import path
from . import views
#adding urls

urlpatterns = [
    path('', views.index, name = "index"),
    path('<int:book_id>/', views.index, name = "index"),
    path('', views.index, name = "index")
]

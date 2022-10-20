from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name="home"),
    path('monitor/', views.traffic_monitor, name="monitor"), #system monitor view to be created next
]
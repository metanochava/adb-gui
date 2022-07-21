
from django.urls import path
from . import views



urlpatterns = [
    path('', views.wellcome, name='home'),
    path('devices', views.devices, name='devices'),
    path('device/<str:id>/', views.device, name='device'),
    path('device/<str:id>/files/', views.files, name='files'),
    path('device/<str:id>/up_down/', views.up_down, name='up_down'),
    path('device/<str:id>/packages/', views.packages, name='packages'),
    path('device/<str:id>/screenshot/', views.screenshot, name='screenshot'),
    path('device/<str:id>/screenrecord/', views.screenrecord, name='screenrecord'),
    path('device/<str:id>/apps/', views.apps, name='apps'),
]


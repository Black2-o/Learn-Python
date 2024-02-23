from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoute),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>', views.getRoom),
]

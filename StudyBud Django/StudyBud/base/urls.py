from django.urls import path, include
from base import views

urlpatterns = [
    path('', views.hello, name="Home"),
    path('room/<str:pk>', views.room, name="Room"),
    path('create-room/', views.create_room, name="Create_ROOM"),
    path('update-room/<str:pk>', views.updateRoom, name="Update_ROOM"),
    path('delete-room/<str:pk>', views.deleteRoom, name="Delete_ROOM"),
    path('login', views.loginPage, name="Login"),
    path('logout', views.logoutuser, name="Logout"),
    path('register', views.registerUser, name="Register"),
    path('delete-messege/<str:pk>', views.deleteMessege, name="Delete_Messege"),
    path('profile/<str:pk>', views.userProfile, name="UserProfile"),
    path('update-user/', views.updateUser, name="UpdateUser"),
    path('topic/', views.topicPage, name='topic'),
    path('activity/', views.activityPage, name='activity')
]

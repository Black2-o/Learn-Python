from django.forms import ModelForm
from .models import User, Room
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomFrom(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserFrom(ModelForm):
    class Meta:
        model = User
        fields = ['avater', 'name', 'username', 'email', 'bio']

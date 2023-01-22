from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Booking


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

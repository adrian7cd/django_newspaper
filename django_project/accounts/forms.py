from sqlite3 import Cursor
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):
  class Meta(UserCreationForm):
    model = CustomUser
    fields = [
      "username",
      "email",
      "age",
    ]

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm):
    model = CustomUser
    fields = [
      "username",
      "email",
      "age",
    ]
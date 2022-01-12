from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import NewUser


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    class Meta:
        model = NewUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

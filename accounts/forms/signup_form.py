from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import User as CustomUser

class SignUpForm(UserCreationForm):
    #email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = CustomUser
        #fields = ('username', 'email', 'password1', 'password2')
        fields = ('username', 'password1', 'password2')

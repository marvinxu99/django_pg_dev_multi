from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User as CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')
        #exclude = ('first_name', 'last_name',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        #exclude = ('first_name', 'last_name',)

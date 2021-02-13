from django.contrib.auth.forms import UserChangeForm, UserCreationForm

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

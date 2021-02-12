from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # home
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

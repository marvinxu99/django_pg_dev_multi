from django.contrib.auth.models import User

"""
Generate a random password.
Code from http://code.activestate.com/recipes/59873-random-password-generation/
"""
import string
import random


def gen_passwd(length=8, chars=string.ascii_letters + string.digits):
    return ''.join([random.choice(chars) for i in range(length)])

def username_present(username):
    if User.objects.filter(username=username).count():
        return True
    
    return False
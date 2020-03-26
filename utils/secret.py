from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
random_string = get_random_string(50, chars)
print(random_string)

'''
Generate a random password.
Code from http://code.activestate.com/recipes/59873-random-password-generation/
'''
import string
import random


def gen_passwd(length=8, chars=string.ascii_letters + string.digits):
    return ''.join([random.choice(chars) for i in range(length)])

def username_present(username):
    if User.objects.filter(username=username).count():
        return True
    
    return False
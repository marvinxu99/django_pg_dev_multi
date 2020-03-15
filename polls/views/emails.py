from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from polls.forms import ContactForm


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['marvinxu99@hotmail.com', 'winnpysoft@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    
    return render(request, 'polls/email_sent.html')

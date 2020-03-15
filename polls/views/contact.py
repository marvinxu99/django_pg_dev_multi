from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from polls.forms import ContactForm


def contact(request):
    
    return render(request, 'polls/contact.html')

def email_contact(request):
    
    # If this is a POST request, we need to process the form data
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            email_from = settings.EMAIL_HOST_USER
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['marvinxu99@hotmail.com', 'winnpysoft@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, email_from, recipients)
            
            ##return HttpResponseRedirect('polls:about' %}")
            return render(request, 'polls/email_sent.html')
    else:
        form = ContactForm()
   
    context = {
            'domain': settings.DOMAIN,
            'form': form,
        }

    return render(request, 'polls/contact.html', context)
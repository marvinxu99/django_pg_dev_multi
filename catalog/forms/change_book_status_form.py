from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# Implement #1 - using forms.Form, see renew_form.py for an example

# Implmemt #2 - The same can be done using the ModelForm
from django.forms import ModelForm
from catalog.models import BookInstance


# class MyForm(forms.Form):
#     myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))

# class MyForm(forms.ModelForm):
#     class Meta:
#         model = MyModel

#     def __init__(self, *args, **kwargs):
#         super(MyForm, self).__init__(*args, **kwargs)
#         self.fields['myfield'].widget.attrs.update({'class' : 'myfieldclass'})


class ChangeBookStatusStaffModelForm(ModelForm):
    class Meta:
        model = BookInstance
        fields = ['status']
        labels = {'status': _('Status')}
        help_texts = {'Status': _('Change the status of the book instance.')}
        # widgets = {
        #     'status': forms.Select(attrs={'size': '10'})
        # }

    # def __init__(self, *args, **kwargs):
    #     super(ChangeBookStatusStaffModelForm, self).__init__(*args, **kwargs)
    #     self.fields['status'].widget.attrs.update({'size' : '10'})

    def clean_status(self):
       data = self.cleaned_data['status']

    #    # Check if a date is not in the past.
    #    if data < datetime.date.today():
    #        raise ValidationError(_('Invalid date - renewal in past'))

    #    # Check if a date is in the allowed range (+4 weeks from today).
    #    if data > datetime.date.today() + datetime.timedelta(weeks=4):
    #        raise ValidationError(_('Invalid date - return date more than 4 weeks ahead'))

       # Remember to always return the cleaned data.
       return data

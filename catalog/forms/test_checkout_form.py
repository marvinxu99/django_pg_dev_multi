from django.forms import ModelForm
from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from catalog.models import BookInstance

# Implement #1 - using forms.Form, see renew_form.py for an example

# Implmemt #2 - The same can be done using the ModelForm


class TestCheckoutModelForm(ModelForm):
    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('Return date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')}
        widgets = {
            'due_back': forms.DateInput(attrs={'class': 'input-sm-field req-field', 'id': 'input_datepicker'})
        }


    def clean_due_back(self):
       data = self.cleaned_data['due_back']

       # Check if a date is not in the past.
       if data < datetime.date.today():
           raise ValidationError(_('Invalid date - renewal in past'))

       # Check if a date is in the allowed range (+4 weeks from today).
       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(_('Invalid date - return date more than 4 weeks ahead'))

       # Remember to always return the cleaned data.
       return data

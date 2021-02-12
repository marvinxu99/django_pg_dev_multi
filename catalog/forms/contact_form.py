from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={ "size":40 })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows":4, "cols":45})
    )
    sender = forms.EmailField(
        label="Your email",
        widget=forms.EmailInput(attrs={ "size":40, 'placeholder':'email@example.com' }),
    )
    cc_myself = forms.BooleanField(label="CC yourself", required=False)

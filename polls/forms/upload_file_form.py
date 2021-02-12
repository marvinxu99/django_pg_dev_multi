from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file_name = forms.FileField()

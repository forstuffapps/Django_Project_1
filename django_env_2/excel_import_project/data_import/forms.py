

# data_import/forms.py

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()




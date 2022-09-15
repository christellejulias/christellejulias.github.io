from unittest.util import _MAX_LENGTH
from django import forms
#form creation

class ContactForm(forms.Form):
    first_name = form.CharField(max_length = 50)
    last_name = form.CharField(max_length = 50)
    email_address = form.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)
	
from django import forms
from django import forms

# File: shayna/august/forms.py

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(max_length=100, label='Subject')
    phone = forms.CharField(max_length=15, required=False, label='Phone')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    



# This form can be used in your views to handle contact form submissions.
# Example usage in a view:
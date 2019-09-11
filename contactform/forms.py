# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(required=True, label='Full Names')
    from_email = forms.EmailField(required=True, label='Email')
    subject = forms.CharField(required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='message')
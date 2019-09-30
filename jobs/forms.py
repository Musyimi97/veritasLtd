from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class': "form-control"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"})),
    class Meta:
        model = Application
        fields =('email', 'subject', 'message', 'document', )
    
        
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea, required=True)

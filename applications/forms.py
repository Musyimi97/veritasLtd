from django import forms
from .models import Applications

class ApplicationForm (forms.ModelForm):
    class Meta:
        model=Applications
        managed = True
        verbose_name = 'Applications'
        verbose_name_plural = 'Applications'
        fields=('name','email_details', 'phone','resume')
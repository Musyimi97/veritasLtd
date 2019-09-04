from django import forms
from .models import Applications
  
     

    
class ApplicationForm (forms.ModelForm):
    CHOICES=[
         ("EMPLOYED", 'employed'),
         ("SELF_EMPLOYED", 'self_employed'),
         ("UNEMPLOYED", "unemployed"),
         ("STUDENT", 'student'),
          ]

    history=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    class Meta:
        model=Applications
        managed = True
        verbose_name = 'Applications'
        verbose_name_plural = 'Applications'
        fields=('name','email_details', 'phone','resume')
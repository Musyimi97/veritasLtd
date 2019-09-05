from django import forms
  
class ResumeForm(forms.Form):
    EXPERIENCE_CHOICES=[
        ('0', '0'),
        ('2', '2'), 
        ('3', '3'),
        ('more than 3', 'MORE THAN 3')
    ]

    name=forms.CharField(required=True),
    from_email=forms.EmailField(required=True),
    experience= forms.ChoiceField(required=False, 
    widgets=forms.RadioSelect,
    choices=EXPERIENCE_CHOICES,
    )
    attach=forms.FileField(widgets=forms.FileInput),    



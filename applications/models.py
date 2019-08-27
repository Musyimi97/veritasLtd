from django.db import models

# Create your models here.
class Applications(models.Model):
    CHOICES=(
        ("EMPLOYED", 'Employed'),
        ("SELF_EMPLOYED", 'Self_employed'),
        ("UNEMPLOYED", "Unemployed"),
        ("STUDENT", 'Student'),

    )

    name=models.CharField( max_length=50)
    email_details=models.EmailField( max_length=254)
    phone=models.PhoneNumberField(default=+254)
    status=models.CharField(max_length=50, choices=CHOICES, default='Unemployed'),
    resume=models.FileField( upload_to='documents/%Y/%m/%d/', max_length=100)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 

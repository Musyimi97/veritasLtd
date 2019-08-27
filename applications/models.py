from django.db import models

# Create your models here.
class Applications(models.Model):
    CHOICES=(
        (0, 'Employed'),
        (1, 'Self_employed'),
        (2, "Unemployed"),
        (3, 'Student'),

    )

    name=models.CharField( max_length=50),
    email_details=models.EmailField( max_length=254),
    phone=models.PhoneNumberField(default=+254),
    employment=models.CharField(choices=CHOICES, max_length=50, )

    def __str__(self):
        return 

    def __unicode__(self):
        return 

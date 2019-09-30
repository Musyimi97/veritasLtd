from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Jobs(models.Model):
    CHOICES = (
        (0, 'Walk-ins'),
        (1, 'BPO'),
        (2, 'Teaching'),
        (3, 'Diploma_jobs'),
        (4, 'Tech_support'),
        (5, 'Finance'),
        (6, 'Part_time'),
        (7, 'Health_care'),
        (8, 'Hospitality'),
        (9, 'Internships'),
        (10, 'Research'),
        (11, 'Security'),
    )
    jobs = models.IntegerField(choices=CHOICES, default=5)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    location =models.CharField(max_length=50, default='Nairobi')

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural= 'Jobs'

    def __str__(self):
        return self.title



class Application(models.Model):
    from_email= models.EmailField()
    subject =models.CharField(max_length=100)
    message =models.CharField(max_length=30)
    document = models.FileField(upload_to='documents/')
    def __str__(self):
        self.email

    class Meta:
        managed = True
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
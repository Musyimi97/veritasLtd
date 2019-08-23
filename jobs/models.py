from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
J
class Jobs(models.Model):
    CHOICES = [
        (0, 'Walk-ins'),
        (1, 'BPO jobs'),
        (2, 'Teaching jobs'),
        (3, 'Diploma jobs'),
        (4, 'Tech support'),
        (5, 'Finance jobs'),
        (6, 'Part time jobs'),
        (7, 'Health care'),
        (8, 'Hospitality'),
        (9, 'Internships'),
        (10, 'Research jobs'),
        (11, 'Security jobs'),
    ],
    jobs = models.CharField(max_length=1, choices=CHOICES)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    location =models.CharField(max_length=50, default='Nairobi')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
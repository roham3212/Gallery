from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length= 20)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, )
    updared_date = models.DateTimeField(auto_now=True)
    statues = models.BooleanField(default=False)

    def __str__(self):
        return self.title
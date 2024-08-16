from django.db import models

class user(models.Model):
    email = models.EmailField(max_length=70)
    message = models.CharField(max_length=3000)    
from django.contrib.auth.models import User
from django.db import models

class Plan(models.Model):
    sarlavha = models.CharField(max_length=50)
    matn = models.CharField(max_length=150)
    sana = models.DateTimeField()
    holat = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):return self.sarlavha

from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    desc = models.TextField()
    status = models.BooleanField(default=False)

from django.db import models

# Create your models here.
class Score(models.Model):
    team = models.CharField(max_length=200)
    blocks1 = models.IntegerField()
    code1 = models.TextField()
    blocks2 = models.IntegerField()
    code2 = models.TextField()
    blocks3 = models.IntegerField()
    code3 = models.TextField()

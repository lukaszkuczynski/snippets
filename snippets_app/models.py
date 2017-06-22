from django.db import models

class Snippet(models.Model):
    language = models.CharField(max_length=20)
    code = models.CharField(max_length=200)
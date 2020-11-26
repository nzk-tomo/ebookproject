from django.db import models

class Ebook(models.Model):
   url = models.CharField(max_length=100)
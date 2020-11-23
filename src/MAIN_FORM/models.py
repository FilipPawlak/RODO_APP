from django.db import models

# Create your models here.
class MainForm(models.Model):
	Imię      = models.CharField(max_length=30)
	Nazwisko  = models.CharField(max_length=30)
	Numer_tel = models.CharField(max_length=12)
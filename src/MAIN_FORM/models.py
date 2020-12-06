from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class MainForm(models.Model):
	Imię      			= models.CharField(max_length=30)
	Nazwisko  			= models.CharField(max_length=30)
	Numer_tel 			= PhoneNumberField()
	ZgodaMarketing   	= models.BooleanField(default=False)
	ZgodaInfHandlowa   	= models.BooleanField(default=False)
	ZgodaMarketingBezp  = models.BooleanField(default=False)
	ZgodaPrzeglad   	= models.BooleanField(default=False)





from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class MainForm(models.Model):
	Imię      			= models.CharField(max_length=30)
	Nazwisko  			= models.CharField(max_length=30)
	Numer_tel 			= PhoneNumberField()
	Data_przegladu		= models.DateField(null=True, blank=True)
	Data_polisy			= models.DateField(null=True, blank=True	)
	ZgodaMarketing   	= models.BooleanField(default=True)
	ZgodaInfHandlowa   	= models.BooleanField(default=True)
	ZgodaMarketingBezp  = models.BooleanField(default=True)
	ZgodaPrzeglad   	= models.BooleanField(default=True)
	NumerZlecenia       = models.CharField(max_length=50, null=True, blank=True)





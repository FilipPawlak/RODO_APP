from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import MainForm

class RodoForm(forms.ModelForm):
	Imię          		    = forms.CharField(label='', 
								  widget = forms.TextInput(
								  attrs = {"placeholder":"Imię"}))
	Nazwisko                = forms.CharField(label='', 
								  widget = forms.TextInput(
								  attrs = {"placeholder":"Nazwisko"}))
	Numer_tel               = PhoneNumberField(widget=forms.TextInput(
									attrs={'placeholder': ('Numer telefonu')}), 
									label=(""))

	ZgodaMarketing          = forms.BooleanField(widget= forms.CheckboxInput(), 
												label=("Wyrażam zgodę na przetwarzanie danych osobowych w celach marketingowych"), 
												label_suffix = (""),
												required = False)
	ZgodaInfHandlowa        = forms.BooleanField(widget= forms.CheckboxInput(), 
												label=("Wyrażam zgodę na przetwarzanie danych osobowych celem przesyłania informacji handlowej"), 
												label_suffix = (""),
												required = False)	
	ZgodaMarketingBezp      = forms.BooleanField(widget= forms.CheckboxInput(), 
												label=("Wyrażam zgodę na przetwarzanie danych osobowych w celach marketingu bezpośredniego"), 
												label_suffix = (""),
												required = False)
	ZgodaPrzeglad           = forms.BooleanField(widget= forms.CheckboxInput(), 
												label=("Wyrażam zgodę na przetwarzanie numeru telefonu celem przypomnienia o terminie badania technicznego lub przeglądu pojazdu"),
												label_suffix = (""),
												required = False)



	

	class Meta:
		model = MainForm
		fields = [
			'Imię',
			'Nazwisko',
			'Numer_tel',
			'ZgodaMarketing',
			'ZgodaInfHandlowa',
			'ZgodaMarketingBezp',
			'ZgodaPrzeglad',
		]





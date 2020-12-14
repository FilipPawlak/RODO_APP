from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import MainForm
from django.utils.safestring import mark_safe


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

	Data_przegladu          = forms.DateField(
									widget=forms.DateInput(
									format='%d/%m/%Y',
									attrs={'class': 'myDateClass',
			  							   'placeholder': 'Data w formacie dd/mm/yyyy'}),
									input_formats=('%d/%m/%Y',),
									)

	Data_polisy          = forms.DateField(
									widget=forms.DateInput(
									format='%d/%m/%Y',
									attrs={'class': 'myDateClass',
			  							   'placeholder': 'Data w formacie dd/mm/yyyy'}),
									input_formats=('%d/%m/%Y',),
									)



	ZgodaMarketing          = forms.BooleanField(widget= forms.CheckboxInput(),
												 initial=True,
												 label=mark_safe('Wyrażam zgodę na przetwarzanie danych osobowych w celach marketingowych (<a href="www.google.com" target="_blank">Treść zgody</a>)'),
												 label_suffix = (""),
												 required = False)

	ZgodaInfHandlowa        = forms.BooleanField(widget= forms.CheckboxInput(),
												 initial=True,
												 label=mark_safe('Wyrażam zgodę na przetwarzanie danych osobowych celem przesyłania informacji handlowej(<a href="www.google.com" target="_blank">Treść zgody</a>)'),
												 label_suffix = (""),
												 required = False)

	ZgodaMarketingBezp      = forms.BooleanField(widget= forms.CheckboxInput(),
												 initial=True,
												 label=mark_safe('Wyrażam zgodę na przetwarzanie danych osobowych w celach marketingu bezpośredniego (<a href="www.google.com" target="_blank">Treść zgody</a>)'),
												 label_suffix = (""),
												 required = False)

	ZgodaPrzeglad           = forms.BooleanField(widget= forms.CheckboxInput(),
												 initial=True,
												 label=mark_safe('Wyrażam zgodę na przetwarzanie numeru telefonu celem przypomnienia o terminie badania technicznego lub przeglądu pojazdu (<a href="www.google.com" target="_blank">Treść zgody</a>)'),
												 label_suffix = (""),
												 required = False)

	NumerZlecenia			= forms.CharField(label='',
											  required=False,
								  			  widget = forms.TextInput(
								              attrs = {"placeholder":"Numer zlecenia"}))

	

	class Meta:
		model = MainForm
		fields = [	
			'Imię',
			'Nazwisko',
			'Numer_tel',
			'Data_przegladu',
			'Data_polisy',
			'ZgodaMarketing',
			'ZgodaInfHandlowa',
			'ZgodaMarketingBezp',
			'ZgodaPrzeglad',
			'NumerZlecenia',
		]





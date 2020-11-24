from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import MainForm

class RodoForm(forms.ModelForm):
	Imię       = forms.CharField(label='', 
								  widget = forms.TextInput(
								  attrs = {"placeholder":"Imię"}))
	Nazwisko       = forms.CharField(label='', 
								  widget = forms.TextInput(
								  attrs = {"placeholder":"Nazwisko"}))
	Numer_tel = PhoneNumberField(widget=forms.TextInput(
									attrs={'placeholder': ('Numer telefonu')}), 
									label=(""))

	class Meta:
		model = MainForm
		fields = [
			'Imię',
			'Nazwisko',
			'Numer_tel'
		]

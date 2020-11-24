from django.shortcuts import render
from .models import MainForm

from .forms import RodoForm

# Create your views here.
def home_view(request, *args, **kwargs):
	form = RodoForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = RodoForm()

	context = {
		'form': form
	}
	return render(request, "home.html", context)
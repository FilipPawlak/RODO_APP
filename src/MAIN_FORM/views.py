from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from RODO_APP.utils import render_to_pdf

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

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': '',
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def pdf_html(request, *args, **kwargs):
	return render(request, "pdf.html")


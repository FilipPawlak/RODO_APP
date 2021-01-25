from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django import forms
from RODO_APP.utils import render_to_pdf
from .forms import RodoForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home_view(request, ticket='', *args, **kwargs):
    form = RodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RodoForm()

    context = {
        'form': form,
        'ticket': ticket,
    }
    return render(request, "home.html", context)


def zlecenie(request, *args, **kwargs):
    context = {}
    return render(request, "zlecenie.html", context)



class TicketForm(forms.Form):
    ticket = forms.CharField()


# def ticket_view(request, ticket=''):
#     form = TicketForm(request.POST)
#     if form.is_valid():
#         if request.method == 'POST':
#             return HttpResponseRedirect('dane/', ticket)
#     else:
#         form = TicketForm(request.POST)
#         return render(request, 'zlecenie.html', {'form': form})


def ticket_view(request, ticket=''):
    form = TicketForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            return HttpResponseRedirect(reverse('home_view',
                                        args=(form.cleaned_data['ticket'],)))
    else:
        form = TicketForm(request.POST)
        return render(request, 'zlecenie.html', {'form': form})


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

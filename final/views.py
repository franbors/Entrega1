from django.http import HttpResponse
from django.shortcuts import render
from customer.models import Cliente
from customer.forms import costumer_form

def index_view(request):
    return render(request, 'index_view.html')


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Contact
from .form import ContForm
# Create your views here.

class Index(CreateView):
    template_name = "main.html"
    model = Contact
    form_class = ContForm
    success_url = reverse_lazy('index')




# def index(request):
#     return render(request,'main.html')
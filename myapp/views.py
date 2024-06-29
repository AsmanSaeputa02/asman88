from django.shortcuts import render
from django.http import HttpResponse
from myapp.admin import Person


def index(request):
    all__person = Person.objects.all()
    return render(request,'index.html',{'all__person':all__person})

def about(request):
    return render(request,'about.html')

def form(request):
    return render(request,'form.html')
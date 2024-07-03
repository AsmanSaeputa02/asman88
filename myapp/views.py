from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.admin import Person
from django.urls import reverse



def about(request):
    return render(request,'about.html')


def     form(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        age = request.POST.get('Age')
        
        # Create a new Person object
        person = Person.objects.create(
            name=name,
            age=age
        )
        
        # Log the created Person object
        print(person, 'Person object created')  # Use Python's print function for logging
        person.save()
        
        return redirect(reverse('index'))
    else:
        return render(request, 'form.html')

def index(request):
    if not Person:
        return render(request, 'index.html')
    else :
        return render(request, 'index.html', {'people': Person.objects.all()}) 


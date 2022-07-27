from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .forms import Contactleads
from .models import ContactForm

# Create your views here.


def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request,'about.html')

def Form(request):
      if request.method =='POST':
            forms = Contactleads(request.POST)
            if forms.is_valid():
                  name = forms.cleaned_data['name']
                  email = forms.cleaned_data['email']
                  location= forms.cleaned_data['location']
                  form = ContactForm(name=name, email=email, location=location)
                  form.save()
                  return HttpResponseRedirect('/')
            else:
                  print('Incorrect data, not saved to db')

      else:
            forms = Contactleads()
      return render(request,'form.html',{"form":forms})
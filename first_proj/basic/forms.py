from django import forms
from .models import ContactForm

class Contactleads(forms.ModelForm):
    name=forms.TextInput()
    email=forms.EmailInput()
    location=forms.TextInput()
    class Meta:
        model = ContactForm
        fields = ['name','email','location']
        labels = {'name': 'Name', 'email': 'Email id','location':'Location'}
        error_messages = {  'name':{'required':'Please enter your full name'},
                            'email':{'required':'Please enter the email id'},
                            'location':{'required':'Please Enter valid location'}
        }
        
        widgets = {
                    'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Candidate name'}),
                    'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Correct Email Id'}),
                    'location': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Location'}),
                    
        }
        
 
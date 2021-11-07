from django import forms
from django.db.models import fields
from . models import Contact

class ContactForm(forms.Form):
     full_name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(
         attrs={'class': 'form-control', 'placeholder': 'Your Name...'}
     ))
     email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(
         attrs={'class': 'form-control', 'placeholder': 'Your Email...'}
     ))
     subject = forms.CharField(label="Subject", max_length=100, widget=forms.TextInput(
         attrs={'class': 'form-control', 'placeholder': 'Subject...'}
     ))
     message = forms.CharField(label='Message', widget=forms.Textarea(
         attrs={'class': 'form-control', 'placeholder': 'Your Message...'}
     ))
        
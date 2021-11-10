from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms.widgets import Widget
from . models import Contact
from  utils.validators import mail_validator
class ContactForm(forms.ModelForm):

    full_name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(
         attrs={'class': 'form-control', 'placeholder': 'Your Name...'}
     ))
    
    email = forms.EmailField(label='Email', max_length=100, validators=(mail_validator,), widget=forms.EmailInput(
         attrs={'class': 'form-control', 'placeholder': 'Your Email...'}
     ))
    message = forms.CharField(label='Message', widget=forms.Textarea(
         attrs={'class': 'form-control', 'placeholder': 'Your Message...'}
     ))
    subject = forms.CharField(label="Subject", max_length=100, widget=forms.TextInput(
         attrs={'class': 'form-control', 'placeholder': 'Subject...'}
     ))
    class Meta:
        model=Contact
        fields='__all__'
        
 #    full_name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(
 #        attrs={'class': 'form-control', 'placeholder': 'Your Name...'}
 #    ))
 #    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(
 #        attrs={'class': 'form-control', 'placeholder': 'Your Email...'}
 #    ))
 #    subject = forms.CharField(label="Subject", max_length=100, widget=forms.TextInput(
 #        attrs={'class': 'form-control', 'placeholder': 'Subject...'}
 #    ))
 #    message = forms.CharField(label='Message', widget=forms.Textarea(
 #        attrs={'class': 'form-control', 'placeholder': 'Your Message...'}
 #    ))
        
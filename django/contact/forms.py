from django import forms
from django.db.models import fields
from contact.utils.validators import mail_validator
from . models import Contact


class ContactForm(forms.ModelForm):

    email = forms.EmailField(label='Email', max_length=100, validators=(mail_validator,), widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Email...'}
    ))
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Name...'}),
            # 'email': forms.EmailInput(
            #     attrs={'class': 'form-control', 'placeholder': 'Your Email...'}),
            'subject': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Subject...'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Your Message...'})
        }

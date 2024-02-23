from django.forms import ModelForm, TextInput
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'f_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Your Name",
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Email",
            }),
            'subject': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Subject",
            }),
            'message': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Message",
            }),
        }


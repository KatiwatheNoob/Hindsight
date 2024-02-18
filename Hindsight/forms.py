from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from .models import SubscribedEmails

#forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)



class SubscribedEmailsForm(forms.ModelForm):
    class Meta:
        model = SubscribedEmails
        fields = ['email']

from django import forms
from django.conf import settings
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from .models import SubscribedEmail

from django_recaptcha.fields import ReCaptchaField


#forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    



class EmailsForm(forms.ModelForm):
    
    captcha = ReCaptchaField()

    class Meta:
        model = SubscribedEmail
        fields = ("email","captcha")


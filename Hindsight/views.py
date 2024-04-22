from django.shortcuts import render, redirect,get_object_or_404

#my Imports
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.core.mail import send_mail,EmailMessage
from django.contrib import messages 
from django.template import loader
from .forms import ContactForm, EmailsForm
from .models import Parcel,Service,SubscribedEmail,MainService,Property, Image
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse

User = get_user_model()





def index(request):
    parcels = Parcel.objects.all()
    mainservices = MainService.objects.all()
 
    return render(request, 'index.html', {'parcels':parcels, 'mainservices':mainservices})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message_subject = request.POST.get('message_subject')
        message = request.POST.get('message')
        
        # send an email
        send_mail(
                message_name, #subject
                message, # message
                message_email, # from email
                {'info@hindsight-ventures.com'}, # to email
        )
        

        return render(request, 'contact.html', {'message_name' :message_name})

    else:
        return render(request, 'contact.html', {})


   
def about(request):
    return render(request, 'about.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services':services})

def careers(request):
    return render(request, 'careers.html')



def subscribe(request):
    if request.method == 'POST':
        Email_form = EmailsForm(request.POST)
        if Email_form.is_valid():
            email = Email_form.cleaned_data['email']
            if SubscribedEmail.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                Email_form.save()
                messages.success(request, "Successfully Subscribed")
        else:
            context = {"Email_form": Email_form}
            return render(request, 'subscribe.html', context=context)

    Email_form = EmailsForm()
    context = {"Email_form": Email_form}
    return render(request, 'subscribe.html', context=context)



def get_quote(request):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Process the form data and send the email
        # You can customize this part based on your needs
          # Retrieve service details
        service = get_object_or_404(Service, id=service_id)

        # Example sending email
        send_mail(
            
            f'Quote Request for {service.name}',
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nService: {service.name}',
            {email},  # Replace with your email address
            ['roykatiwa@gmail.com'],  # Replace with the recipient's email address
            fail_silently=False,
        )

        # You can also save the form data to the database or perform other actions

        return render(request, 'services.html', {})

    
def property_grid(request):
    properties = Property.objects.all()

    # Add a default image URL for each property
    for property in properties:
        default_image = property.images.first()  # Assuming the first image is the default
        property.default_image_url = default_image.image.url if default_image else 'path/to/default/image.jpg'

    return render(request, 'property_grid.html', {'properties': properties})

def property_single(request, property_id=None):
    if property_id:
        # Retrieve the specific property using its ID
        property = get_object_or_404(Property, pk=property_id)

        # Retrieve images associated with the property
        images = property.images.all()

        # Get the main image URL
        main_image_url = images.first().image.url if images.exists() else 'path/to/default/image.jpg'

        # Get the Google Maps URL
        google_maps_url = property.google_maps_url

        return render(request, 'property_single.html', {'property': property, 'images': images, 'main_image_url': main_image_url, 'google_maps_url': google_maps_url})
    else:
        # Handle the case where property_id is not provided
        # You might want to display an error message or redirect to another page
        return render(request, 'index.html', {'message': 'Property ID not provided'})


def send_email_to_agent(request):
    property_id = None  # Default value for property_id

    if request.method == 'POST':
        property_id = request.POST.get('property_id')  # Assuming property_id is included in the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('message')

        # Build the email message
        subject = f'Property Inquiry - Property ID: {property_id}'
        message = f'Name: {name}\nEmail: {email}\nComment: {comment}'

        # Send the email
        send_mail(
            subject,
            message,
            email,  # Replace with your "from" email address
            ['roykatiwa@gmail.com'],  # Replace with the agent's email address
            fail_silently=False,
        )

        # Optionally, you can redirect the user after sending the email
        return render(request, 'property_single.html', {'name': name})
   














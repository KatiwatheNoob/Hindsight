from django.urls import path
from . import views
from .views import get_quote,send_email_to_agent


#Pages
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('careers/', views.careers, name='careers'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('get_quote/', get_quote, name='get_quote'),
  

    path('property_single/', views.property_single, name='property_single'),  # Without property_id
    path('property_single/<int:property_id>/', views.property_single, name='property_single_with_id'),  # With property_id
    path('property_grid/', views.property_grid, name='property_grid'),
    path('send_email_to_agent/', send_email_to_agent, name='send_email_to_agent'),
]


    

    

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings


#OPT options (for development)#########################################//Later under construction
from django.contrib.auth.models import User
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin


class OTPAdmin(OTPAdminSite):
   pass

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)
##########################################################################3


urlpatterns = [
    path('admin/', admin.site.urls), #(add - admin_site instead of admin.)to avoid error
    path('', include('Hindsight.urls')),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

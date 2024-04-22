from django.contrib import admin
from .models import Category, Parcel, Service, SubscribedEmail, MainService,  Property,Image


class SubscribedEmailsAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')  # Fix: Use underscore instead of space



admin.site.register(Category)
admin.site.register(Parcel)
admin.site.register(Service)
admin.site.register(SubscribedEmail, SubscribedEmailsAdmin)  # Register SubscribedEmails with the custom admin class
admin.site.register(MainService)


class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'formatted_price', 'location', 'size_of_land', 'land_unit', 'category', 'structures', 'video', 'google_maps_url')

    def formatted_price(self, obj):
        # Format the price with commas
        return "{:,}".format(obj.price)
    formatted_price.short_description = 'Price'
    def get_category(self, obj):
        # Access the related category's name
        return obj.category.name if obj.category else None
    get_category.short_description = 'Category'


admin.site.register(Image)

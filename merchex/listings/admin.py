from django.contrib import admin

from listings.models import Band
from listings.models import Listing

# Register your models here.
admin.site.register(Band)
admin.site.register(Listing)

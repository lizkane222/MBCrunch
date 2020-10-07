from django.contrib import admin
from .models import Bin, Person, Investor, Collection_Market

# Register your models here.

admin.site.register(Bin)
admin.site.register(Person)
admin.site.register(Investor)
admin.site.register(Collection_Market)
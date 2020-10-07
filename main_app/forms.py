from django.forms import ModelForm
from .models import Bin, Person, Investor, Collection_Market

class Bin_Form(ModelForm):
    class Meta:
        model = Bin
        fields = ['type',]


class Person_Form(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'bio',]


class Investor_Form(ModelForm):
    class Meta:
        model = Investor
        fields = ['name','bio','current_location','bin']


class Collection_Market_Form(ModelForm):
    class Meta:
        model = Collection_Market
        fields = [ 'name', 'dates', 'time_start', 'time_end','location','market_description',]
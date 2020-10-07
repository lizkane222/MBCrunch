from django.forms import ModelForm
from .models import Bin, Person, Investor, Collection_Market

class Bin_Form(ModelForm):
    class Meta:
        model = Bin
        fields = ['type','location','delivery_date','delivery_location','verified','gives_rewards',]


class Person_Form(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'bio', 'deposits_made', 'verifications', 'current_location', 'identify_new_bin', 'rewards', 'community_contributions','bins',]


class Investor_Form(ModelForm):
    class Meta:
        model = Investor
        fields = ['name','bio','deposits_made','verifications','current_location','identify_new_bin','gives_rewards','bin']


class Collection_Market_Form(ModelForm):
    class Meta:
        model = Collection_Market
        fields = [ 'name', 'dates', 'time_start', 'time_end', 'investors',]
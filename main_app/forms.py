from django.forms import ModelForm
from .models import Bin, Investor

class Bin_Form(ModelForm):
    class Meta:
        model = Bin
        fields = ['type','location','collection_market','delivery_date','delivery_location','verified','sponsor','gives_rewards',]

class Investor_Form(ModelForm):
    class Meta:
        model = Investor
        fields = ['name','bio','deposits_made','community_contributions','verifications','current_location','sponsor','identify_new_bin','gives_rewards',]
# Import Django forms module
from django import forms

# Import the Donation model from the current app's models
from .models import Donation


# Define a form for the Donation model using ModelForm
class DonationForm(forms.ModelForm):
    class Meta:
        # Specify the model to be used for this form
        model = Donation
        # Specify the fields to be included in the form
        fields = ['name', 'email', 'amount', 'message']

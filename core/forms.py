from django import forms
from .models import UserMessage


# Form for UserMessage model
class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage  # Model to use
        fields = '__all__'  # Include all fields

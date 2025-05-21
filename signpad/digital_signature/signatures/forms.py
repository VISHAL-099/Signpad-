from django import forms
from .models import UserSignature

class UserSignatureForm(forms.ModelForm):
    class Meta:
        model = UserSignature
        fields = ['name', 'age']  # Include signature field

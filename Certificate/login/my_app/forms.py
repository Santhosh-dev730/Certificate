from django import forms
from .models import certificate

class certificate_form(forms.ModelForm):
    class Meta:
        model = certificate
        fields = ['reg_no', 'name', 'email','course','trainer']
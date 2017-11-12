from django import forms
from product.models import Catering

class ContactForm(forms.ModelForm):
    class Meta:
        model = Catering
        exclude = [""]
        fields = ['name', 'phone', 'subject', 'details']
from django import forms
from product.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = [""]
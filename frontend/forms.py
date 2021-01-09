from django.forms import fields, forms,ModelForm
from contact.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'

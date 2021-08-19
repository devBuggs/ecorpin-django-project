from django import forms

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('contact_name', 'contact_mobile', 'contact_email', 'contact_type', 'contact_date', 'project_title', 'project_idea')
        labels = {
            'project_title': 'Title',
            'project_idea': 'Description',
            'contact_type': 'Contact Medium',
            'contact_date': 'Contact Date',
            'contact_email': 'Email',
            'contact_mobile': 'Phone',
            'contact_name': 'Name'
        }


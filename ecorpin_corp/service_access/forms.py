from django import forms

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('project_title', 'project_idea', 'contact_date', 'contact_email', 'contact_mobile', 'contact_name', 'contact_type')
        labels = {
            'project_title': 'Project Title',
            'project_idea': 'Project Idea',
            'contact_type': 'Contact Medium',
            'contact_date': 'Date of Contact',
            'contact_email': 'Contact Email',
            'contact_mobile': 'Contact Number',
            'contact_name': 'Name'
        }
        
        #exclude = ['feedback_Date'] #feedback date and time label
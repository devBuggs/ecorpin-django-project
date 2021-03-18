from django import forms

from .models import feedback

class feedback_form(forms.ModelForm):
    class Meta:
        model = feedback
        fields = (
            'visitor_name',
            'visitor_organization',
            'visitor_email',
            'feedback_msg'
        )
        required = (
            'visitor_name',
            'visitor_organization',
            'visitor_email',
            'feedback_msg'
        )
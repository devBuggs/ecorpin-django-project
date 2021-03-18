from django import forms

from .models import feedback

class feedback_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

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
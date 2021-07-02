from django import forms

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('visitor_name', 'visitor_organization', 'visitor_email', 'feedback_msg')
        labels = {
            'visitor_name':'Full Name',
            'visitor_organization':'Company/Organization',
            'visitor_email':'Email Address',
            'feedback_msg':'Feedback/Suggestion/Idea Message'
        }
        
        #exclude = ['feedback_Date'] #feedback date and time label
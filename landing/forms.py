# landing/forms.py
from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(required=True)
    your_subject = forms.CharField(required=True)
    your_message = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}))
    cc_myself = forms.BooleanField(required=False)
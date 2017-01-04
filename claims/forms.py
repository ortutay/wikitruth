from django import forms

from . import models

class NewClaimForm(forms.Form):
    thesis = forms.CharField(max_length=200, required=True)
    body = forms.CharField(widget=forms.Textarea, max_length=10000, required=True)
    direction = forms.ChoiceField(choices=models.DIRECTION_CHOICES)

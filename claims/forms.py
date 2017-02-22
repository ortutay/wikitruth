from django import forms

from . import models
from models import Claim


class NewClaimForm(forms.Form):
    thesis = forms.CharField(max_length=200, required=True)
    body = forms.CharField(widget=forms.Textarea, max_length=10000, required=True)
    direction = forms.ChoiceField(choices=models.DIRECTION_CHOICES)

    def clean(self):
        super(NewClaimForm, self).clean()
        self.cleaned_data['citations'] = clean_citations(self.data.getlist('citations'))


class ResponseForm(forms.Form):
    direction = forms.ChoiceField(choices=models.DIRECTION_CHOICES)
    body = forms.CharField(widget=forms.Textarea, max_length=10000, required=True)

    def clean(self):
        super(ResponseForm, self).clean()
        self.cleaned_data['citations'] = clean_citations(self.data.getlist('citations'))


# TODO(ortutay): I think this is possible to do via CitationField(forms.Field)?
def clean_citations(citations):
    for claim_id in citations:
        Claim.objects.get(pk=claim_id)
    return citations

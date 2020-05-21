from django import forms
from ghostapp.models import VoteChoice

class VoteChoiceForm(forms.Form):
    choice = forms.BooleanField(required=False)
    text = forms.CharField(max_length=280)
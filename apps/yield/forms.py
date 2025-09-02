from django import forms
from .models import Yield

class YieldForm(forms.ModelForm):
    class Meta:
        model = Yield
        fields = ['crop', 'livestock', 'quantity', 'date']

from django import forms

from .models import Sections

class SectionsForm(forms.ModelForm):

    class Meta:
        model = Sections
        fields = ('number', 'professor', 'course')

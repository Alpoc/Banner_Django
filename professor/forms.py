from django import forms

from .models import ProfessorName

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = ProfessorName
        fields = ('name',)

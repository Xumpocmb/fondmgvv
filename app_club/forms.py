from django import forms
from tinymce.widgets import TinyMCE
from .models import Club

class ClubForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Club
        fields = ['name', 'description', 'military_unit', 'date_of_founding', 'city', 'region', 'main_picture']

from django import forms
from tinymce.widgets import TinyMCE
from .models import News


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = News
        fields = ['title', 'content',  'main_picture', 'created_at']
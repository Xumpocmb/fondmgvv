from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Ваше имя')
    email = forms.EmailField(required=True, label='Ваш email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Ваш вопрос')

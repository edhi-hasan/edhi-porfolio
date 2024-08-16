from django import forms

class contact(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    message = forms.CharField(widget=forms.Textarea, label='Message')

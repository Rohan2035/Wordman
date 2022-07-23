from django import forms
from keeper import models

class addPasswordForms(forms.ModelForm):
    
    key = forms.CharField(widget=forms.PasswordInput())

    class Meta:

        model = models.password_store
        fields = ['password_label', 'password']

        widgets = {

            'password' : forms.PasswordInput(),
        }
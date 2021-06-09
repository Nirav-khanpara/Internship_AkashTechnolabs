from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class StudentRegi(forms.Form):
    
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re-Password',widget=forms.PasswordInput)
    agree = forms.BooleanField(label='I Agree to the terms and conditions ', label_suffix='')

    def clean(self):
        cleaned_data = super().clean()
        name_value = self.cleaned_data['name']
        val1 = self.cleaned_data['password']
        val2 = self.cleaned_data['rpassword']

        if val1!=val2:
            raise ValidationError('passwords are not matching !!!')

        if name_value[0].islower():
            raise forms.ValidationError('First character must be capital.')

        

    

    

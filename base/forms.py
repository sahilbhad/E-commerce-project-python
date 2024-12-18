from django import forms
from .models import checkout


class ch_form(forms.ModelForm):
    class  Meta:
        model=checkout
        fields=['fullname','address','phonenumber','city','state','zipcode']
 
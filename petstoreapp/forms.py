from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet 
        fields = ['name', 'breed', 'price', 'image']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'breed' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.TextInput(attrs={'class':'form-control'}),
        }

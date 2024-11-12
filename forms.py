from django import forms
from .models import MakeupProduct

class MakeupProductForm(forms.ModelForm):
    class Meta:
        model = MakeupProduct
        fields = ['name', 'category', 'brand', 'price', 'stock', 'description']

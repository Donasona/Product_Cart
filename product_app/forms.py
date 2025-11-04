from django import forms
from product_app.models import Productmodel

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productmodel
        fields = ["name","price","stock"]

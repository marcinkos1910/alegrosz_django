from django import forms

from product import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = "__all__"

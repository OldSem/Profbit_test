from django import forms
from django.db import models



class ProductsForm(forms.Form):
    products = forms.Field()



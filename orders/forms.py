from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Petro"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Petrenko"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "you@example.com"
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Ukraine, Kyiv, Centre str., 123"
    }))

    class Meta:
        model = Order
        fields = (
            "first_name",
            "last_name",
            "email",
            "address"
        )
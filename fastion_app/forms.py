# yourapp/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import SignupData
from .models import Order
# Worldwide country code choices (partial list, can be expanded)
COUNTRY_CODE_CHOICES = [
    ('+1', 'United States (+1)'),
    ('+44', 'United Kingdom (+44)'),
    ('+91', 'India (+91)'),
    ('+880', 'Bangladesh (+880)'),
    ('+61', 'Australia (+61)'),
    ('+81', 'Japan (+81)'),
    ('+49', 'Germany (+49)'),
    ('+33', 'France (+33)'),
    ('+971', 'UAE (+971)'),
    ('+966', 'Saudi Arabia (+966)'),
    # Add more as needed
]

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class SignupDataForm(forms.ModelForm):
    country_code = forms.ChoiceField(choices=COUNTRY_CODE_CHOICES, required=True)

    class Meta:
        model = SignupData
        fields = ['country_code', 'phone_number', 'address']  # ✅ fixed the field name
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']
        widgets = {
            'payment_method': forms.Select(choices=Order._meta.get_field('payment_method').choices)
        }
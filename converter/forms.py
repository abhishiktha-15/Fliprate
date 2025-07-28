from django import forms

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('INR', 'Indian Rupee'),
    ('GBP', 'British Pound'),
    ('JPY', 'Japanese Yen'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
]

class CurrencyForm(forms.Form):
    amount = forms.DecimalField(label="Amount", min_value=0, decimal_places=2)
    from_currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label="From")
    to_currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label="To")
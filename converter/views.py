from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from .forms import CurrencyForm

API_KEY = "50595d7248fee2e5d7c86bc3"

def converter_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_curr = form.cleaned_data['from_currency']
            to_curr = form.cleaned_data['to_currency']
            try:
                url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_curr}/{to_curr}/{amount}"
                response = requests.get(url, timeout=5)
                data = response.json()
                if data.get('result') == 'success':
                    result = round(data['conversion_result'], 2)
                else:
                    error = "API error: " + data.get("error-type", "Unknown error")
            except Exception:
                error = "Failed to fetch rates. Please try again."
        else:
            error = "Please check the entered values."
    else:
        form = CurrencyForm()

    return render(request, 'converter/converter.html', {
        'form': form,
        'result': result,
        'error': error
    })
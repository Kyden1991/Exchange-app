from django.shortcuts import render
import requests
from collections import OrderedDict
from .fusioncharts import FusionCharts


def charts(request):
    response = requests.get(url='https://v6.exchangerate-api.com/v6/8f1e1e724cb81ce7b73d1412/latest/USD').json()
    currencies = response.get('conversion_rates')
    from_curr = request.POST.get('from-curr')
    to_curr = request.POST.get('to-curr')
    if request.method == 'GET':
        context = {
            'currencies': currencies,
            'from_curr': from_curr,
            'to_curr': to_curr
        }
        return render(request=request, template_name='exchange_app/index.html', context=context)

    # charts API
    url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "5xOq13VSvLzq0AtKjUkV7mGZLgF6T1Td"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text



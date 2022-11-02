from django.shortcuts import render
import requests
import json
from datetime import datetime, timedelta


def charts(request):
    end_date = datetime.now().date()
    start_date = datetime.now().date() - timedelta(days=30)
    base_currency = 'USD'
    url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={start_date}&end_date={end_date}&base={base_currency}"
    payload = {}
    headers = {
        "apikey": "5xOq13VSvLzq0AtKjUkV7mGZLgF6T1Td"
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()

    if request.method == 'GET':
        response_currencies = requests.get(url='https://v6.exchangerate-api.com/v6/8f1e1e724cb81ce7b73d1412/latest/USD').json()
        currencies = response_currencies.get('conversion_rates')
        context = {
            'currencies': currencies
        }

        return render(request=request, template_name="charts_app/charts.html", context=context)


    # create list with dates
    days_list_json = response.get('rates').keys()
    day_list = list(days_list_json)

    # year : The title for horizontal axis
    h_var = 'Period'

    # price : The title for horizontal axis
    v_var = f'USD'

    # data : A list of list which will ultimated be used
    # to populate the Google chart.
    data = [[h_var,v_var]]
    """
    An example of how the data object looks like in the end: 
        [
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]
    The first list will consists of the title of horizontal and vertical axis,
    and the subsequent list will contain coordinates of the points to be plotted on
    the google chart
    """

    for i in range(len(day_list)):
        price = response['rates'][f'{day_list[i]}']['USD']
        data.append([day_list[i], price])


    # h_var_JSON : JSON string corresponding to  h_var
    # json.dumps converts Python objects to JSON strings
    h_var_JSON = json.dumps(h_var)

    # v_var_JSON : JSON string corresponding to  v_var
    v_var_JSON = json.dumps(v_var)

    # modified_data : JSON string corresponding to  data
    modified_data = json.dumps(data)
    chart_render = {
        'values': modified_data,
        'h_title': h_var_JSON,
        'v_title': v_var_JSON
    }



    return render(request, "charts_app/charts.html", chart_render)









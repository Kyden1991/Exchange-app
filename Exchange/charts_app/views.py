from django.shortcuts import render
import requests
import json
from datetime import datetime, timedelta


def charts(request):
    if request.method == 'GET':

        return render(request=request, template_name='exchange_app/index.html')

    if request.method == 'POST':

        end_date = datetime.now().date()
        start_date = datetime.now().date() - timedelta(days=30)
        print('end ', end_date)
        print('start ', start_date)
        url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={start_date}&end_date={end_date}"
        payload = {}
        headers = {
            "apikey": "5xOq13VSvLzq0AtKjUkV7mGZLgF6T1Td"
        }

        response = requests.request("GET", url, headers=headers, data=payload).json()

        # create list with dates
        days_list_json = response.get('rates').keys()
        day_list = list(days_list_json)

        # year : The title for horizontal axis
        h_var = 'Period'

        # price : The title for horizontal axis
        v_var = 'Price'

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
            price = response['rates'][f'{day_list[i]}']['AED']
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








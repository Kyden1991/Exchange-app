from django.shortcuts import render
import requests
from collections import OrderedDict
from .fusioncharts import FusionCharts


def charts(request):
    # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Country"
    chartConfig["yAxisName"] = "Reserves (MMbbl)"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    dataSource["data"].append({"label": 'Venezuela', "value": '290'})
    dataSource["data"].append({"label": 'Saudi', "value": '290'})
    dataSource["data"].append({"label": 'Canada', "value": '180'})
    dataSource["data"].append({"label": 'Iran', "value": '140'})
    dataSource["data"].append({"label": 'Russia', "value": '115'})
    dataSource["data"].append({"label": 'Russia', "value": '115'})
    dataSource["data"].append({"label": 'UAE', "value": '100'})
    dataSource["data"].append({"label": 'US', "value": '30'})
    dataSource["data"].append({"label": 'China', "value": '300'})

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    return render(request, 'charts_app/charts.html', {
        'output': column2D.render()
    })

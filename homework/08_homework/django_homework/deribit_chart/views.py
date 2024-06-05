from django.shortcuts import render
from django.http import JsonResponse
import time
import requests
import pandas as pd

# Create your views here.
def home(request):
    return render(request, '../templates/home.html')

def api_deribit(request):
    url = "https://www.deribit.com/api/v2/public/get_tradingview_chart_data"

    start_time = 0
    end_time = int(time.time() * 1000)  # Current time in milliseconds

    # Define the parameters
    params = {
        "instrument_name": 'BTC-PERPETUAL',
        "start_timestamp": start_time,
        "end_timestamp": end_time,
        "resolution": 60
    }
    
    # Send the GET request
    response = requests.get(url, params=params)

    data = response.json()  # Parse the response to JSON
    # Write data to the database
    ohlc = pd.DataFrame()
    ohlc["timestamp"] = pd.to_datetime(data['result']['ticks'], unit='ms')
    ohlc["open"] = data['result']['open']
    ohlc["high"] = data['result']['high']
    ohlc["low"] = data['result']['low']
    ohlc["close"]= data['result']['close']
    ohlc["cost"] = data['result']['cost']
    ohlc["volume"] = data['result']['volume']
    ohlc['instrument_name'] = 'BTC-PERPETUAL'
    ohlc['resolution'] = 60
    chart_data = [{'date': entry['timestamp'].isoformat(), 'open': entry['open'], 'close': entry['close']} for entry in ohlc.to_dict('records')]
    return JsonResponse(chart_data, safe=False)

def chart_page(request):
    return render(request, '../templates/chart.html')
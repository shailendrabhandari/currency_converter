import requests

API_URL = "http://apilayer.net/api/live"
API_KEY = "you_api_key_here"
VALID_CURRENCIES = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "JPY", "CNY", "CHF"]

# Function to get a single exchange rate
def get_conversion_rate(from_currency, to_currency):
    params = {
        'access_key': API_KEY,
        'currencies': to_currency,
        'source': from_currency,
        'format': 1
    }
    response = requests.get(API_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data from API: {response.status_code}")
    
    data = response.json()
    
    # Check for error in the response
    if 'error' in data:
        raise Exception(f"API Error: {data['error']}")
    
    rate_key = f"{from_currency}{to_currency}"
    return data['quotes'].get(rate_key)

# Function to get exchange rates for multiple currencies
def get_multiple_exchange_rates(from_currency, to_currencies):
    """
    Fetch exchange rates from 'from_currency' to multiple 'to_currencies'.
    """
    currencies = ",".join(to_currencies)
    params = {
        'access_key': API_KEY,
        'currencies': currencies,
        'source': from_currency,
        'format': 1
    }
    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Error fetching data from API: {response.status_code}")

    data = response.json()
    
    # Check for error in the response
    if 'error' in data:
        raise Exception(f"API Error: {data['error']}")

    rates = {f"{from_currency}{to_currency}": data['quotes'].get(f"{from_currency}{to_currency}") for to_currency in to_currencies}
    return rates
import requests

API_URL = "https://v6.exchangerate-api.com/v6/your_API/latest"
VALID_CURRENCIES = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "JPY", "CNY", "CHF"]

# Function to get a single exchange rate
def get_conversion_rate(from_currency, to_currency):
    url = f"{API_URL}/{from_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data from API: {response.status_code}")
    
    data = response.json()

    # Check for error in the response
    if data.get('result') != 'success':
        raise Exception(f"API Error: {data.get('error-type')}")
    
    return data['conversion_rates'].get(to_currency)

# Function to get exchange rates for multiple currencies
def get_multiple_exchange_rates(from_currency, to_currencies):
    """
    Fetch exchange rates from 'from_currency' to multiple 'to_currencies'.
    """
    url = f"{API_URL}/{from_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching data from API: {response.status_code}")

    data = response.json()

    # Check for error in the response
    if data.get('result') != 'success':
        raise Exception(f"API Error: {data.get('error-type')}")

    rates = {to_currency: data['conversion_rates'].get(to_currency) for to_currency in to_currencies}
    return rates


# Example usage
try:
    print(get_conversion_rate("USD", "EUR"))  # Fetch conversion rate from USD to EUR
    print(get_multiple_exchange_rates("USD", ["EUR", "GBP", "INR"]))  # Fetch conversion rates for multiple currencies
except Exception as e:
    print(e)
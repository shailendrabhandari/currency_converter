from api import get_conversion_rate

def convert_currency(from_currency, to_currency, amount):
    rate = get_conversion_rate(from_currency, to_currency)
    if rate is None:
        raise ValueError(f"Cannot find conversion rate for {to_currency}")
    return amount * rate

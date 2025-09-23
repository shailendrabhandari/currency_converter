import emoji
VALID_CURRENCIES = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "JPY", "CNY", "CHF"]

def validate_currency_code(currency_code):
    if currency_code not in VALID_CURRENCIES:
        raise ValueError(f"Invalid currency code: {currency_code}")


# Mapping of currency codes to country flags using emoji shortcodes
CURRENCY_FLAGS = {
    "USD": emoji.emojize(":United_States:"),
    "EUR": emoji.emojize(":European_Union:"),
    "GBP": emoji.emojize(":United_Kingdom:"),
    "INR": emoji.emojize(":India:"),
    "AUD": emoji.emojize(":Australia:"),
    "CAD": emoji.emojize(":Canada:"),
    "SGD": emoji.emojize(":Singapore:"),
    "JPY": emoji.emojize(":Japan:"),
    "CNY": emoji.emojize(":China:"),
    "CHF": emoji.emojize(":Switzerland:"),
}

def get_currency_flag(currency_code):
    """
    Get the flag for the given currency code.
    """
    return CURRENCY_FLAGS.get(currency_code, "")
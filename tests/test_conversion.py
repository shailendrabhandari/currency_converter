import pytest
from conversion import convert_currency

# Mock function to replace get_conversion_rate
def mock_get_conversion_rate(from_currency, to_currency):
    if from_currency == "USD" and to_currency == "EUR":
        return 0.85
    if from_currency == "USD" and to_currency == "GBP":
        return 0.75
    return None

# Test currency conversion
def test_convert_currency(monkeypatch):
    # Mock the get_conversion_rate function
    monkeypatch.setattr('conversion.get_conversion_rate', mock_get_conversion_rate)

    # Test conversion from USD to EUR
    result = convert_currency("USD", "EUR", 100)
    assert result == 85.0  # 100 USD * 0.85 EUR rate

    # Test conversion from USD to GBP
    result = convert_currency("USD", "GBP", 100)
    assert result == 75.0  # 100 USD * 0.75 GBP rate

    # Test conversion with an invalid currency pair
    with pytest.raises(ValueError):
        convert_currency("USD", "XYZ", 100)

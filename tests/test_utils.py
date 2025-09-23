import pytest
from utils import validate_currency_code, get_currency_flag

# Test currency code validation
def test_validate_currency_code():
    # Test valid currency codes
    validate_currency_code("USD")  # Should not raise an error
    validate_currency_code("EUR")  # Should not raise an error

    # Test invalid currency code
    with pytest.raises(ValueError):
        validate_currency_code("XYZ")  # Should raise ValueError

# Test getting currency flags
def test_get_currency_flag():
    # Test with valid currency codes
    assert get_currency_flag("USD") == "🇺🇸"
    assert get_currency_flag("EUR") == "🇪🇺"

    # Test with an unsupported currency
    assert get_currency_flag("XYZ") == ""

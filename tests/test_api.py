import pytest
import requests
from api import get_conversion_rate, get_multiple_exchange_rates

# Mock data for testing
mock_api_response_single = {
    'quotes': {
        'USDEUR': 0.85
    }
}

mock_api_response_multiple = {
    'quotes': {
        'USDEUR': 0.85,
        'USDGBP': 0.75
    }
}

# Mock the requests.get call itself
def mock_requests_get_single(url, params):
    class MockResponse:
        def json(self):
            return mock_api_response_single
        status_code = 200
    return MockResponse()

def mock_requests_get_multiple(url, params):
    class MockResponse:
        def json(self):
            return mock_api_response_multiple
        status_code = 200
    return MockResponse()

# Test the get_conversion_rate function
def test_get_conversion_rate(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get_single)
    rate = get_conversion_rate('USD', 'EUR')
    assert rate == 0.85

# Test the get_multiple_exchange_rates function
def test_get_multiple_exchange_rates(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get_multiple)
    rates = get_multiple_exchange_rates('USD', ['EUR', 'GBP'])
    assert rates['USDEUR'] == 0.85
    assert rates['USDGBP'] == 0.75

# Currency Conversion Module
import requests
from datetime import datetime, timedelta
import json

class CurrencyConverter:
    def __init__(self, cache_file='temp/currency_cache.json'):
        self.cache_file = cache_file
        self.cache_duration = 3600  # 1 hour
        self.api_url = 'https://api.exchangerate-api.com/v4/latest'
        self.base_currency = 'USD'
        self.supported_currencies = ['USD', 'INR', 'EUR', 'GBP', 'AUD', 'CAD', 'SGD', 'AED', 'JPY']

    def get_exchange_rates(self):
        """Get current exchange rates"""
        # Try cache first
        rates = self._load_from_cache()
        if rates:
            return rates
        
        try:
            response = requests.get(f"{self.api_url}/{self.base_currency}")
            if response.status_code == 200:
                data = response.json()
                rates = data.get('rates', {})
                self._save_to_cache(rates)
                return rates
        except Exception as e:
            print(f"Error fetching exchange rates: {e}")
        
        # Return default rates if API fails
        return self._get_default_rates()

    def convert(self, amount, from_currency='USD', to_currency='INR'):
        """Convert amount from one currency to another"""
        if from_currency == to_currency:
            return amount
        
        rates = self.get_exchange_rates()
        
        # Convert to base currency first (USD)
        if from_currency != self.base_currency:
            amount = amount / rates.get(from_currency, 1)
        
        # Convert to target currency
        converted = amount * rates.get(to_currency, 1)
        
        return round(converted, 2)

    def _load_from_cache(self):
        """Load rates from cache file"""
        try:
            import os
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r') as f:
                    data = json.load(f)
                    if datetime.fromisoformat(data['timestamp']) > datetime.now() - timedelta(seconds=self.cache_duration):
                        return data['rates']
        except Exception as e:
            print(f"Error loading cache: {e}")
        return None

    def _save_to_cache(self, rates):
        """Save rates to cache file"""
        try:
            import os
            os.makedirs('temp', exist_ok=True)
            with open(self.cache_file, 'w') as f:
                json.dump({
                    'rates': rates,
                    'timestamp': datetime.now().isoformat()
                }, f)
        except Exception as e:
            print(f"Error saving cache: {e}")

    def _get_default_rates(self):
        """Return default exchange rates"""
        return {
            'USD': 1.0,
            'INR': 83.12,
            'EUR': 0.92,
            'GBP': 0.79,
            'AUD': 1.52,
            'CAD': 1.36,
            'SGD': 1.34,
            'AED': 3.67,
            'JPY': 149.50
        }

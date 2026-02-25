import requests

class CoinGeckoClient:
    
    def __init__(self):
        
        self.base_url = "https://api.coingecko.com/api/v3"
        
    def fetch_price(self, crypto_id):
       
        endpoint = f"{self.base_url}/simple/price" 
        params = {
            'ids': crypto_id,
            'vs_currencies': 'usd',
            'include_24hr_change': 'true'
            
        }
        
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
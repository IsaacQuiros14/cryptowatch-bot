import requests

class CryptoCollectorError(Exception):
    
    pass                                

class CryptoCollector:
 
    
    def __init__(self, api_client, date_manager):
        
        self.api_client = api_client
        self.date_manager = date_manager
    
    def get_current_price(self, symbol):
      
        try:
           
            response = self.api_client.fetch_price(symbol)
        
            if symbol in response and 'usd' in response[symbol]:
                return float(response[symbol]['usd'])
            
            return None
            
        except Exception as e:
            
            print(f"Error fetching price for {symbol}: {e}")
            
            return None
    
    def get_multiple_prices(self, symbols):
      
        return {
            
            symbol: self.get_current_price(symbol) 
            
            for symbol in symbols
            
        }
    
    def get_timestamp(self):
        
        return self.date_manager.get_current_timestamp()
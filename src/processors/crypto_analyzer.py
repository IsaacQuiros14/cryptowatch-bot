class CryptoAnalyzer:
  
    
    def __init__(self, collector):
       
        self.collector = collector

    def filter_by_price_threshold(self, symbols, threshold=1000):
        
        prices = self.collector.get_multiple_prices(symbols)
        
        return {
            symbol: price 
            for symbol, price in prices.items() 
            if price and price >= threshold
        }

    def get_top_gainers(self, market_data, top_n=3):
     
        return sorted(
            market_data, 
            key=lambda x: x.get('change_24h', 0), 
            reverse=True
        )[:top_n]
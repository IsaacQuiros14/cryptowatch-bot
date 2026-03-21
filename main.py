import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.utils.date_manager import DateManager
from src.api.coingecko_client import CoinGeckoClient
from src.collectors.crypto_collector import CryptoCollector
from src.processors.crypto_analyzer import CryptoAnalyzer
from src.storage.csv_handler import CSVHandler
from src.storage.db_manager import DBManager
from src.processors.data_validator import DataValidator, DataValidationError

def main():
    print("CRYPTOWATCH BOT - SQL PRO EDITION")
    print("-" * 50)

    date_manager = DateManager()
    api_client = CoinGeckoClient()
    collector = CryptoCollector(api_client, date_manager)
    analyzer = CryptoAnalyzer(collector)
    
    csv_handler = CSVHandler()
    db = DBManager()
    
    raw_prices = {}
    symbols = ['bitcoin', 'ethereum', 'solana', 'cardano', 'polkadot']
    
    
    try:
        raw_prices = collector.get_multiple_prices(symbols)
        
        validated_prices = DataValidator.validate_prices(raw_prices)
        
        csv_handler.append_price_batch(validated_prices)
        db.insert_prices_batch(validated_prices)
        
        latest = db.get_latest_prices()
        
    except DataValidationError as e:
        print(f"\n ADVERTENCIA DE CALIDAD: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
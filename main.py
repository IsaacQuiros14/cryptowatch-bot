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

def main():
    print("CRYPTOWATCH BOT - SQL PRO EDITION")
    print("-" * 50)

    date_manager = DateManager()
    api_client = CoinGeckoClient()
    collector = CryptoCollector(api_client, date_manager)
    analyzer = CryptoAnalyzer(collector)
    
    csv_handler = CSVHandler()
    db = DBManager()
    
    try:
        symbols = ['bitcoin', 'ethereum', 'solana', 'cardano', 'polkadot']
 
        print(f"EXTRACT: Consultando precios para: {', '.join(symbols)}")
        prices = collector.get_multiple_prices(symbols)
    
        print("\nLOAD: Guardando datos...")
     
        csv_handler.append_price_batch(prices)

        db.insert_prices_batch(prices)
     
        print("\n" + "="*50)
        print("ESTADISTICAS SQL (REPORTES)")
        print("="*50)

        latest = db.get_latest_prices()
        for record in latest:
            print(f" {record['symbol'].upper():10} | DB Price: ${record['price']:>12,.2f}")
            
        print("-" * 50)
        print("PIPELINE EJECUTADO EXITOSAMENTE")

    except Exception as e:
        print(f"ERROR CRITICO: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
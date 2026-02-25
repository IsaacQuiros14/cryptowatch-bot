import sys
import os
from pathlib import Path

# Configuración de rutas para que Python encuentre 'src'
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.utils.date_manager import DateManager
from src.api.coingecko_client import CoinGeckoClient
from src.collectors.crypto_collector import CryptoCollector
from src.processors.crypto_analyzer import CryptoAnalyzer

def main():
    print("🚀 CRYPTOWATCH BOT - CONECTANDO A LA RED...")
    
    # Inicialización de componentes (Dependency Injection)
    date_manager = DateManager()
    api_client = CoinGeckoClient()
    collector = CryptoCollector(api_client, date_manager)
    analyzer = CryptoAnalyzer(collector)
    
    try:
        symbols = ['bitcoin', 'ethereum', 'solana']
        print(f"📊 Obteniendo precios reales para: {symbols}")
        
        # Llamada real a la API
        prices = collector.get_multiple_prices(symbols)
        
        print("\n" + "="*40)
        print("💰 PRECIOS EN TIEMPO REAL")
        print("="*40)
        for symbol, price in prices.items():
            if price:
                print(f"   ✅ {symbol.upper():8} : ${price:,.2f} USD")
            else:
                print(f"   ❌ {symbol.upper():8} : Error al obtener dato")
        print("="*40)

    except Exception as e:
        print(f"❌ Error crítico en el flujo: {e}")

if __name__ == "__main__":
    main()
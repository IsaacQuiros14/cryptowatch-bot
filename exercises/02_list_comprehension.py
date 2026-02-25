# ============================================
# EJERCICIO LIST COMPREHENSION - CryptoWatch Bot
# ============================================

# Datos simulados de criptomonedas
crypto_data = [
    {"name": "Bitcoin", "symbol": "BTC", "price": 45000, "change_24h": 2.5, "volume": 28000000000},
    {"name": "Ethereum", "symbol": "ETH", "price": 2500, "change_24h": -1.2, "volume": 15000000000},
    {"name": "Cardano", "symbol": "ADA", "price": 0.48, "change_24h": 3.8, "volume": 800000000},
    {"name": "Solana", "symbol": "SOL", "price": 98, "change_24h": -2.1, "volume": 2000000000},
    {"name": "Polkadot", "symbol": "DOT", "price": 7.2, "change_24h": 5.4, "volume": 600000000},
    {"name": "Dogecoin", "symbol": "DOGE", "price": 0.08, "change_24h": 1.1, "volume": 500000000},
    {"name": "Ripple", "symbol": "XRP", "price": 0.52, "change_24h": -0.5, "volume": 1200000000},
]

# ============================================
# EJERCICIO 1: Filtrar cryptos con precio > $1
# ============================================
def get_expensive_cryptos(data):
    return [crypto for crypto in data if crypto["price"] > 1]


# ============================================
# EJERCICIO 2: Extraer solo los símbolos (BTC, ETH, etc.)
# ============================================
def get_symbols(data):
    Symbols = [crypto["symbol"]for crypto in data]
    return Symbols




def get_gainers(data):
    return [crypto for crypto in data if crypto["change_24h"]> 0 ]


# ============================================
# EJERCICIO 4: Crear lista de nombres en mayúsculas
# ============================================
def get_uppercase_names(data):
   return [crypto["name"].upper() for crypto in data]
   


# ============================================
# EJERCICIO 5: Calcular precios con descuento del 10%
# ============================================
def calculate_discounted_prices(data):
    return[
        {
            "name" : c["name"],
            "original" : c["price"],
            "discounted": c["price"] * 0.9   
        }
        for c in data
        
    ]



# ============================================
# EJERCICIO 6 (AVANZADO): Filtrar y transformar
# ============================================
def get_high_volume_symbols(data, min_volume=1000000000):
    return [c["symbol"].upper() for c in data if c["volume"] > min_volume]

# ============================================
# ZONA DE PRUEBAS
# ============================================
if __name__ == "__main__":
    print("="*60)
    print("EJERCICIOS LIST COMPREHENSION - CryptoWatch Bot")
    print("="*60)
    
    # Ejercicio 1
    print("\n1. Cryptos con precio > $1:")
    expensive = get_expensive_cryptos(crypto_data)
    for crypto in expensive:
        print(f"   {crypto['name']}: ${crypto['price']}")
    
    # Ejercicio 2
    print("\n2. Símbolos de todas las cryptos:")
    symbols = get_symbols(crypto_data)
    print(f"   {symbols}")
    
    # Ejercicio 3
    print("\n3. Cryptos con cambio positivo (24h):")
    gainers = get_gainers(crypto_data)
    for crypto in gainers:
        print(f"   {crypto['name']}: +{crypto['change_24h']}%")
    
    # Ejercicio 4
    print("\n4. Nombres en MAYÚSCULAS:")
    uppercase_names = get_uppercase_names(crypto_data)
    print(f"   {uppercase_names}")
    
    # Ejercicio 5
    print("\n5. Precios con 10% descuento:")
    discounted = calculate_discounted_prices(crypto_data)
    for item in discounted[:3]:  # Solo primeras 3
        print(f"   {item['name']}: ${item['original']} → ${item['discounted']:.2f}")
    
    # Ejercicio 6
    print("\n6. Símbolos con alto volumen (>$1B):")
    high_volume = get_high_volume_symbols(crypto_data)
    print(f"   {high_volume}")
from datetime import datetime, timedelta
import pytz

transactions = [
    {"crypto": "BTC", "amount": 1.5, "price": 45000},
    {"crypto": "ETH", "amount": 10, "price": 2500},
    {"crypto": "ADA", "amount": 1000, "price": 0.5},
]

trades = [
    {"symbol": "BTC", "date": datetime(2026, 2, 10, tzinfo=pytz.UTC), "profit": 500},
    {"symbol": "ETH", "date": datetime(2026, 2, 5, tzinfo=pytz.UTC), "profit": -200},
    {"symbol": "BTC", "date": datetime(2026, 2, 14, tzinfo=pytz.UTC), "profit": 300},
    {"symbol": "SOL", "date": datetime(2026, 2, 8, tzinfo=pytz.UTC), "profit": 150},
    {"symbol": "ADA", "date": datetime(2026, 2, 1, tzinfo=pytz.UTC), "profit": 100},
]

def get_recent_profitable_symbols(trade_data, days_back=7):
    """Filters unique symbols with positive profit within a timeframe."""
    now = datetime.now(pytz.UTC)
    deadline = now - timedelta(days=days_back)

    profitable_cryptos = [
        t["symbol"].upper() 
        for t in trade_data 
        if t["profit"] > 0 and t["date"] > deadline
    ]
    
    return list(set(profitable_cryptos))
    
def calculate_totals(transaction_data):
    """Calculates total USD value for each transaction."""
    return [
        {"crypto": t["crypto"], "total_usd": t["amount"] * t["price"]}
        for t in transaction_data
    ]

def was_weekend_x_days_ago(days):
    """Checks if the date from X days ago was a weekend."""
    past_date = datetime.now() - timedelta(days=days)
    day_number = past_date.weekday()

    return day_number >= 5


days_to_check = 5
is_weekend = was_weekend_x_days_ago(days_to_check)
print(f"Was it a weekend {days_to_check} days ago?: {is_weekend}")

portfolio_results = calculate_totals(transactions)
for item in portfolio_results:
    print(f"{item['crypto']}: ${item['total_usd']:,.2f}")

recent_profitable = get_recent_profitable_symbols(trades, days_back=7)
print(f"Profitable symbols in the last 7 days: {recent_profitable}")
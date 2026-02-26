import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class DBManagerError(Exception):
    pass    

class DBManager:
    
    
    def __init__(self, db_name = "cryptowatch.db"):
        self.db_path = Path ("data/processed") / db_name
        self.db_path.parent.mkdir(parents=True, exist_ok= True)
        self._init_db()
        
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        return conn 
    
    def _init_db(Self):
        with Self._get_connection() as conn:
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS crypto_prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME NOT NULL,
                    symbol TEXT NOT NULL,
                    price REAL NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_symbol_timestamp 
                ON crypto_prices(symbol, timestamp DESC)
            """)
            
            conn.commit()
        print(f"DATABASE: Inicializada en {Self.db_path}")
        
    def insert_prices_batch(Self, prices_data: Dict[str, float], timestamp: Optional[datetime]= None ):
        
        if timestamp is None:
            timestamp = datetime.now()
            
            
        records = [
            (timestamp,  symbol, price)
            for symbol,  price in prices_data.items()
            if price is not None
        ]
        
        if not records:
            return
        
        
        
        try: 
            with Self._get_connection() as conn:
                conn.executemany(
                    "INSERT INTO crypto_prices ( timestamp, symbol, price ) VALUES (?, ? , ? )",
                    records
                    
                )
                conn.commit()
            print(f"STORAGE: Insertados {len(records)} registros en base de datos.")  
        except sqlite3.Error as e: 
            raise DBManagerError(f"Fallo en insercion masivi: {e}")
    def get_latest_prices(Self) -> List[Dict]: 
        
        query = """
            SELECT p1.symbol, p1.price, p1.timestamp
            FROM crypto_prices p1
            INNER JOIN (
                SELECT symbol, MAX(timestamp) as max_timestamp
                FROM crypto_prices
                GROUP BY symbol
            ) p2 ON p1.symbol = p2.symbol AND p1.timestamp = p2.max_timestamp
        """  
        with Self._get_connection()as conn:
            cursor = conn.execute(query)
            return [dict(row) for row in cursor.fetchall()] 
        
    def get_statics(Self, symbol: str, days: int = 7 ) -> Dict:
        """Calcula agregaciones estadisticas usando SQL nativo."""
        query = """
            SELECT 
                COUNT(*) as count,
                ROUND(AVG(price), 2) as avg_price,
                MIN(price) as min_price,
                MAX(price) as max_price
            FROM crypto_prices
            WHERE symbol = ?
            AND timestamp >= datetime('now', '-' || ? || ' days')
        """
        with Self._get_connection() as conn:
            cursor = conn.execute(query,(symbol, days))
            row = cursor.fetchone()
            return dict(row) if row else {}
         
        
        
        
        
        
        
        
        

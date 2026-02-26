import csv
from pathlib import Path
from datetime import datetime

class CSVHandler:
 
    
    def __init__(self, base_path='data'):
        self.base_path = Path(base_path)
        self.processed_path = self.base_path / 'processed'      
        self.processed_path.mkdir(parents=True, exist_ok=True)

    def append_price_batch(self, prices_data):
        
        file_path = self.processed_path / "prices_history.csv"
        file_exists = file_path.exists()
    
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     
        rows = []
        for symbol, price in prices_data.items():
            if price is not None:
                rows.append({
                    'timestamp': timestamp,
                    'symbol': symbol,
                    'price': price
                })

        if not rows:
            return

        with open(file_path, mode='a', newline='') as f:
            fieldnames = ['timestamp', 'symbol', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
           
            if not file_exists:
                writer.writeheader()
            
            writer.writerows(rows)
            
        print(f"STORAGE: Guardados {len(rows)} registros en CSV.")
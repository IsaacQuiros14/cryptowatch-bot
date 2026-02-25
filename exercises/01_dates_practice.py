from datetime import datetime, timedelta
import pytz

def get_current_timestamp():
    
    return datetime.now(pytz.utc)

def format_date(dt):
    if not isinstance(dt, datetime):
        return "Formato invalido"
    return dt.strftime("%Y-%m-%d %H:%M:%S")
 


def get_date_range(days_back=7):
    now_reference = get_current_timestamp()
    start_date = now_reference - timedelta(days= days_back)
    return start_date, now_reference 

if __name__ == "__main__":
    print("="*50)
    print("EJERCICIOS DATES - CryptoWatch Bot")
    print("="*50)
    
   
    print("\n1. Timestamp actual:")
    current = get_current_timestamp()
    print(current)
 
    print("\n2. Fecha formateada:")
    formatted = format_date(current)
    print(formatted)
    
    print("\n3. Rango últimos 7 días:")
    start, end = get_date_range(7)
    print(f"Inicio: {format_date(start)}")
    print(f"Fin: {format_date(end)}")
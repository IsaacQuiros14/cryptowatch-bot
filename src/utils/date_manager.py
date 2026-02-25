from datetime import datetime, timedelta
import pytz

class DateManagerError(Exception):
    pass

class DateManager:
    def __init__(self, timezone='UTC'):
        try:
            self.timezone = pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            raise DateManagerError(f"Zona horaria inválida: {timezone}")
    
    def get_current_timestamp(self):
        return datetime.now(pytz.UTC)
    
    def format_timestamp(self, dt, format_str='%Y-%m-%d %H:%M:%S'):
        if not isinstance(dt, datetime):
            raise DateManagerError(f"Se esperaba datetime, recibido: {type(dt)}")
        try:
            return dt.strftime(format_str)
        except ValueError as e:
            raise DateManagerError(f"Formato inválido '{format_str}': {e}")
    
    def get_timestamp_range(self, days_back=7):
        if days_back <= 0:
            raise DateManagerError("days_back debe ser mayor a 0")
        end_date = self.get_current_timestamp()
        start_date = end_date - timedelta(days=days_back)
        return start_date, end_date
    
    def unix_to_datetime(self, unix_timestamp):
        try:
            unix_timestamp = float(unix_timestamp)
            return datetime.fromtimestamp(unix_timestamp, tz=pytz.UTC)
        except (ValueError, TypeError, OSError) as e:
            raise DateManagerError(f"Unix timestamp inválido '{unix_timestamp}': {e}")
    
    def get_hours_ago(self, hours):
        if hours < 0:
            raise DateManagerError("hours no puede ser negativo")
        return self.get_current_timestamp() - timedelta(hours=hours)
    
    def is_recent(self, timestamp, hours=24):
        if not isinstance(timestamp, datetime):
            raise DateManagerError(f"Se esperaba datetime, recibido: {type(timestamp)}")
        cutoff = self.get_hours_ago(hours)
        return timestamp >= cutoff

    def validate_date_range(self, start_date, end_date):
        if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
            raise DateManagerError("Ambas fechas deben ser datetime")
        if start_date > end_date:
            raise DateManagerError("start_date no puede ser mayor que end_date")
        return True

if __name__ == "__main__":
    dm = DateManager()
    print("=" * 30)
    print("DateManager v2 - Output")
    print("=" * 30)
    
    current = dm.get_current_timestamp()
    print(f"Current: {dm.format_timestamp(current)}")
    
    try:
        dm.unix_to_datetime("abc")
    except DateManagerError as e:
        print(f"Error Test: {e}")
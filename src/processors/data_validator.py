class DataValidationError(Exception):
    
    
    
    
    
    """Excepcion para errores de integridad en los datos de los precios."""
    pass # Las excepciones suelen estar vacías, solo sirven para dar un nombre al error.

class DataValidator:
    @staticmethod
    def validate_prices(prices_data: dict) -> dict:
        """
        Actaua como un filtro de calidad.
        Recibe los datos crudos de la API y solo deja pasar los que son numeros positivos.
        """
        validated = {}
        
        for symbol, price in prices_data.items():
            if not isinstance(price, (int, float)):
                continue
         
            if DataValidator.MIN_REASONABLE_PRICE < price < DataValidator.MAX_REASONABLE_PRICE:
                validated[symbol] = price
            else:
                print(f"DEBUG: Precio de {symbol} ({price}) fuera de rango.")
            
    
        if not validated:
            raise DataValidationError("No se recibieron datos de precios válidos.")
            
        return validated
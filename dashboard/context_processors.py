from datetime import datetime
from babel.dates import format_datetime
import pytz

def current_datetime(request):
    # Define la zona horaria de Ecuador
    timezone = pytz.timezone('America/Guayaquil')
    
    # Obtén la fecha y hora actual en la zona horaria de Ecuador
    current_datetime = datetime.now(timezone)
    
    # Formatea la fecha y hora en español
    formatted_datetime = format_datetime(current_datetime, format="EEEE d 'de' MMMM 'del' yyyy - HH:mm", locale='es_ES')
    
    return {
        'current_datetime': formatted_datetime,
    }

import datetime

def get_fecha_actual():
    date =  datetime.datetime.now()
    return date.strftime('%H:%M - %d/%m/%y')

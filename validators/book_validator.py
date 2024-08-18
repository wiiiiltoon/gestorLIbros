import constants.k_dictionary_keys as k_dictionary_keys
import constants.k_atributes as k_atributes
from flask import abort

def validar(data_libro):
    missing_keys = k_dictionary_keys.KEYS_LIBRO_ATRIBUTOS_OBLIGATORIOS - data_libro.keys()
    extra_keys = data_libro.keys() - k_dictionary_keys.KEYS_LIBRO_ATRIBUTOS
    if missing_keys:
        return f'Los atributos {', '.join(missing_keys)} son obligatorios'
    if extra_keys:
        return f'Los atributos {', '.join(extra_keys)} no aplican para libro'
def validar_valoracion(data):
    keys_data = data.keys()
    if k_atributes.LIBRO_VALORACION not in keys_data:
        return f'El atributo {k_atributes.LIBRO_VALORACION} es obligatorio'
    rating = data[k_atributes.LIBRO_VALORACION]
    if not rating:
        return f'El atributo {k_atributes.LIBRO_VALORACION} no puede ser vacio'
    try:
        if int(rating) > 5:
            return f'El valor del atributo {k_atributes.LIBRO_VALORACION} no puede ser superior a 5'
    except ValueError:
        return f'El atributo {k_atributes.LIBRO_VALORACION} debe ser un valor numerico'


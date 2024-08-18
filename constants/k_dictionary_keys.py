import constants.k_endpoints as k_endpoints
import constants.k_atributes as k_atributes

KEYS_LIBRO_ATRIBUTOS_OBLIGATORIOS = {k_atributes.LIBRO_TITULO, k_atributes.LIBRO_AUTOR}
KEYS_LIBRO_ATRIBUTOS = KEYS_LIBRO_ATRIBUTOS_OBLIGATORIOS | {k_atributes.LIBRO_FECHA_INICIO, k_atributes.LIBRO_FECHA_FIN, k_atributes.LIBRO_VALORACION, k_atributes.LIBRO_OPINION}
KEYS_LIBRO_ENDPOINTS = {k_endpoints.CONSULTAR_LIBROS, k_endpoints.AGREGAR_LIBRO, k_endpoints.MODIFICAR_LIBRO, k_endpoints.ELIMINAR_LIBRO, k_endpoints.RANKING_LIBRO, k_endpoints.FICHATECNICA_LIBRO,k_endpoints.VALORAR_LIBRO}
    
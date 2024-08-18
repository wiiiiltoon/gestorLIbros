from flask import Flask, request, jsonify, abort
import constants.k_endpoints as k_endpoints
import constants.k_generales as k_generales
import constants.k_listados as k_listados
import services.libro_servicio as libro_servicio
import entities.Libro as Libro
import list_entities.Libros as Libros
import utilities.messages_errors as message_errors
from urllib.parse import urljoin

app = Flask(__name__)
class_libros = Libros.Libros()

@app.route(k_generales.MENU)
def mostrar_menu():
    base = f'http://{k_generales.HOST}:{k_generales.PORT_FLASK}/'
    endpoint_dict = {}
    for i, endpoint in enumerate(k_listados.LISTADO_LIBRO_ENDPOINTS):
        key = i + 1
        value = urljoin(base, endpoint)
        endpoint_dict[key] = value
    return jsonify(endpoint_dict)

@app.route(k_endpoints.CONSULTAR_LIBRO_BY_ID)
def get_libro_by_id(id_libro):
    libro = libro_servicio.get_libro_by_id(id_libro)
    if libro is None:
        return abort(400, description=message_errors.message_not_found(Libro.LIT_LIBRO, id_libro))
    return jsonify(libro.build())

@app.route(k_endpoints.CONSULTAR_LIBROS)
def get_all_libros():
    libros = libro_servicio.get_all_libros()
    libros_json = [libro.build() for libro in libros]
    return jsonify(libros_json)

@app.route(k_endpoints.AGREGAR_LIBRO,methods=['POST'])
def insert_libro():
    data = request.get_json()
    libro = libro_servicio.insert_libro(data)
    return jsonify(libro.build())

@app.route(k_endpoints.ELIMINAR_LIBRO, methods=['DELETE'])
def delete_libro(id_libro):
    libro = libro_servicio.delete_libro(id_libro)
    if libro is None:
        return abort(400, description=message_errors.message_not_found(Libro.LIT_LIBRO, id_libro))
    return jsonify(libro.build())

@app.route(k_endpoints.MODIFICAR_LIBRO, methods=['PUT'])
def update_libro(id_libro):
    data = request.get_json()
    libro = libro_servicio.update_libro(id_libro, data)
    if libro is None:
        return abort(400, description=message_errors.message_not_found(Libro.LIT_LIBRO, id_libro))
    return jsonify(libro.build())

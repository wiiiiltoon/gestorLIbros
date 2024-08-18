from flask import Flask, request, jsonify, abort
import constants.k_endpoints as k_endpoints
import constants.k_general as k_general
import constants.k_dictionary_keys as k_dictionary_keys
import services.libro_servicio as libro_servicio
import entities.Libro as Libro
import list_entities.Libros as Libros
import utilities.messages_errors as message_errors
import validators.book_validator as book_validator
from urllib.parse import urljoin

app = Flask(__name__)
class_libros = Libros.Libros()

@app.route(k_endpoints.MENU)
def mostrar_menu():
    base = f'http://{k_general.HOST}:{k_general.PORT_FLASK}/'
    endpoint_dict = {}
    for i, endpoint in enumerate(list(k_dictionary_keys.KEYS_LIBRO_ENDPOINTS)):
        key = i + 1
        value = urljoin(base, endpoint)
        endpoint_dict[key] = value
    return jsonify(endpoint_dict)

@app.route(k_endpoints.CONSULTAR_LIBRO_BY_ID)
def get_libro_by_id(id_libro):
    libro = libro_servicio.get_libro_by_id(id_libro)
    is_libro_not_found(id_libro, libro)
    return jsonify(libro.build())

@app.route(k_endpoints.CONSULTAR_LIBROS)
def get_all_libros():
    libros = libro_servicio.get_all_libros()
    libros_json = [libro.build() for libro in libros]
    return jsonify(libros_json)

@app.route(k_endpoints.AGREGAR_LIBRO,methods=['POST'])
def insert_libro():
    data = request.get_json()
    validar_libro(book_validator.validar,data)
    libro = libro_servicio.insert_libro(data)
    return jsonify(libro.build())

@app.route(k_endpoints.ELIMINAR_LIBRO, methods=['DELETE'])
def delete_libro(id_libro):
    libro = libro_servicio.delete_libro(id_libro)
    is_libro_not_found(id_libro, libro)
    return jsonify(libro.build())

@app.route(k_endpoints.MODIFICAR_LIBRO, methods=['PUT'])
def update_libro(id_libro):
    data = request.get_json()
    validar_libro(book_validator.validar,data)
    libro = libro_servicio.update_libro(id_libro, data)
    is_libro_not_found(id_libro, libro)
    return jsonify(libro.build())

@app.route(k_endpoints.VALORAR_LIBRO, methods=['PUT'])
def valorar_libro(id_libro):
    data = request.get_json()
    validar_libro(book_validator.validar_valoracion,data)
    libro = libro_servicio.valorar_libro(id_libro, data)
    is_libro_not_found(id_libro, libro)
    return jsonify(libro.build())


def is_libro_not_found(id_libro, libro):
     if libro is None:
        return abort(400, description=message_errors.message_not_found(Libro.LIT_LIBRO, id_libro))
     
def validar_libro(function, data):
    invalido = function(data)
    if invalido:
        return abort(400, description=invalido)
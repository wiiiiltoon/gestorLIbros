from flask import Flask, request, jsonify, abort
from const_endpoints import *
from const_generales import *
from Libro import *
import libro_servicio
from Libros import *
import Libros
from urllib.parse import urljoin

app = Flask(__name__)
class_libros = Libros.Libros()

@app.route(MENU)
def mostrar_menu():
    base = f'http://{HOST}:{PORT_FLASK}/'
    endpoint_dict = {}
    for i, endpoint in enumerate(LISTADO_LIBRO_ENDPOINTS):
        key = i + 1
        value = urljoin(base, endpoint)
        endpoint_dict[key] = value
    return jsonify(endpoint_dict)

@app.route(CONSULTAR_LIBRO_BY_ID)
def get_libro_by_id(id_libro):
    libro = libro_servicio.get_libro_by_id(id_libro)
    if libro is None:
        return abort(400, description='No se ha encontrado libro con ese id')
    return jsonify(libro.build())
@app.route(CONSULTAR_LIBROS)
def get_all_libros():
    libros = libro_servicio.get_all_libros()
    libros_json = [libro.build() for libro in libros]
    return jsonify(libros_json)

@app.route(AGREGAR_LIBRO,methods=['POST'])
def insert_libro():
    data = request.get_json()
    libro = libro_servicio.insert_libro(data)
    return jsonify(libro.build())

@app.route(ELIMINAR_LIBRO, methods=['DELETE'])
def delete_libro(id_libro):
    libro = libro_servicio.delete_libro(id_libro)
    if libro is None:
        return abort(400, description='No se ha encontrado libro con ese id')
    return jsonify(libro.build())

@app.route(MODIFICAR_LIBRO, methods=['PUT'])
def update_libro(id_libro):
    data = request.get_json()
    libro = libro_servicio.update_libro(id_libro, data)
    if libro is None:
        return abort(400, description='No se ha encontrado libro con ese id')
    return jsonify(libro.build())

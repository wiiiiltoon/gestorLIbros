from entities.Libro import Libro
import constants.k_atributes as k_atributes
import list_entities.Libros as Libros

class_libros = Libros.Libros()

def get_libro_by_id(id_libro):
    return class_libros.get_libro_by_id(id_libro)

def get_all_libros():
    return class_libros.get_libros()

def insert_libro(data):
    titulo = data['title']
    autor = data['author']
    return class_libros.insert_libro(Libro(titulo, autor))

def update_libro(id_libro, data):
    return class_libros.update_libro(id_libro, data)

def delete_libro(id_libro):
    return class_libros.delete_libro(id_libro)

def valorar_libro(id_libro, data):
    rating = data[k_atributes.LIBRO_VALORACION]
    return class_libros.valorar_libro(id_libro, rating)

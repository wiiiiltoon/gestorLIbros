from Libro import Libro
from Libros import *

class_libros = Libros()

def get_libro_by_id(id_libro):
    return class_libros.get_libro_by_id(id_libro)

def get_all_libros():
    return class_libros.get_libros()

def insert_libro(data_libro):
    titulo = data_libro['title']
    autor = data_libro['author']
    return class_libros.insert_libro(Libro(titulo, autor))

def update_libro(id_libro, data_libro):
    return class_libros.update_libro(id_libro, data_libro)

def delete_libro(id_libro):
    return class_libros.delete_libro(id_libro)

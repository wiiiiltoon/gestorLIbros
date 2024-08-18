import entidades.Libro as Libro
from consts_listados import *

class Libros:

    def __init__(self):
        self.libros = []
    
    def get_libro_by_id(self, id_libro):
        libro_eliminado = None
        for libro in self.libros:
            if str(libro.id) == id_libro:
                libro_eliminado = libro
        return libro_eliminado
    
    def get_libros(self):
        return self.libros

    def insert_libro(self, libro):
        self.libros.append(libro)
        return libro

    def delete_libro(self, id_libro):
        libro = self.get_libro_by_id(id_libro)
        if not libro is None:
            self.libros.remove(libro)
        return libro
    
    def update_libro(self, id_libro, atributos):
        libro = self.get_libro_by_id(id_libro)
        for atr in LISTADO_LIBRO_ATRIBUTOS:
            if atr in atributos and atributos[atr] != '' and getattr(libro, atr) != atributos[atr]:
                setattr(libro, atr, atributos[atr])
        return libro
        
import entities.Libro as Libro
import constants.k_atributes as k_atributes
import constants.k_dictionary_keys as k_dictionary_keys

class Libros:

    def __init__(self):
        self.list_libros = []
    
    def get_libro_by_id(self, id_libro):
        libro_eliminado = None
        for libro in self.list_libros:
            if str(libro.id) == id_libro:
                libro_eliminado = libro
        return libro_eliminado
    
    def get_libros(self):
        return self.list_libros

    def insert_libro(self, libro):
        self.list_libros.append(libro)
        return libro

    def delete_libro(self, id_libro):
        libro = self.get_libro_by_id(id_libro)
        if libro is not None:
            self.list_libros.remove(libro)
        return libro
    
    def update_libro(self, id_libro, atributos):
        libro = self.get_libro_by_id(id_libro)
        if libro is not None:
            for atr in list(k_dictionary_keys.KEYS_LIBRO_ATRIBUTOS):
                setattr(libro, atr, atributos[atr])
        return libro
    
    def valorar_libro(self, id_libro, rating):
        libro = self.get_libro_by_id(id_libro)
        if libro is not None:
            setattr(libro, k_atributes.LIBRO_VALORACION, rating)
        return libro
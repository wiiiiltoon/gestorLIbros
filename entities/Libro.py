from constants.k_atributos import *
from utilities.utils import get_fecha_actual
import uuid

class Libro:

    def __init__(self, titulo, autor):
        self._id = uuid.uuid4()
        self._titulo = titulo
        self._autor = autor
        self._fecha_inic = get_fecha_actual()
        self._fecha_fin = ''
        self._opinion = ''
        self._valoracion = ''

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def fecha_inic(self):
        return self._fecha_inic

    @property
    def fecha_fin(self):
        return self._fecha_fin

    @property
    def opinion(self):
        return self._opinion

    @property
    def valoracion(self):
        return self._valoracion
        
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
        
    @autor.setter
    def autor(self, autor):
        self._autor = autor
        
    @fecha_inic.setter
    def fecha_inic(self, fecha_inic):
        self._fecha_inic = fecha_inic
        
    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        self._fecha_fin = fecha_fin
        
    @opinion.setter
    def opinion(self, opinion):
        self._opinion = opinion
        
    @valoracion.setter
    def valoracion(self, valoracion):
        self._valoracion = valoracion
    
    def build(self):
        return {
            LIBRO_ID: str(self.id),
            LIBRO_TITULO: self.titulo,
            LIBRO_AUTOR: self.autor,
            LIBRO_FECHA_INICIO: self.fecha_inic,
            LIBRO_FECHA_FIN: self.fecha_fin,
            LIBRO_VALORACION: self.opinion,
            LIBRO_OPINION: self.valoracion
        }
import constants.k_atributes as k_atributes
from utilities.utils import get_fecha_actual
import uuid

LIT_LIBRO = 'libro'

class Libro:

    def __init__(self, title, author):
        self._id = uuid.uuid4()
        self._title = title
        self._author = author
        self._date_inic = get_fecha_actual()
        self._date_fin = ''
        self._opinion = ''
        self._rating = ''

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def date_inic(self):
        return self._date_inic

    @property
    def date_fin(self):
        return self._date_fin

    @property
    def opinion(self):
        return self._opinion

    @property
    def rating(self):
        return self._rating
        
    @title.setter
    def title(self, title):
        self._title = title
        
    @author.setter
    def author(self, author):
        self._author = author
        
    @date_inic.setter
    def date_inic(self, date_inic):
        self._date_inic = date_inic
        
    @date_fin.setter
    def date_fin(self, date_fin):
        self._date_fin = date_fin
        
    @opinion.setter
    def opinion(self, opinion):
        self._opinion = opinion
        
    @rating.setter
    def rating(self, rating):
        self._rating = rating
    
    def build(self):
        return {
            k_atributes.LIBRO_ID: str(self.id),
            k_atributes.LIBRO_TITULO: self.title,
            k_atributes.LIBRO_AUTOR: self.author,
            k_atributes.LIBRO_FECHA_INICIO: self.date_inic,
            k_atributes.LIBRO_FECHA_FIN: self.date_fin,
            k_atributes.LIBRO_VALORACION: self.rating,
            k_atributes.LIBRO_OPINION: self.opinion
        }
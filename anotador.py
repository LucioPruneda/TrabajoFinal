#! /usr/bin/python3
from nota import Nota


class Anotador:
    '''Representa una colección de Notas que se pueden etiquetar, modificar, y
    buscar'''

    def __init__(self):
        '''Inicializa el anotador con una lista vacía de Notas'''
        self.notas = []
        self.notas.append(Nota("Estudiar Ingles", "Urquiza"))
        self.notas.append(Nota("Comprar pan", "super"))
        self.notas.append(Nota("Llevar a Rita a la veterinaria", "Veronica"))
        # Para facilitar las pruebas, podrías inicializarlo con dos o tres
        # notas precargadas, para evitar cargarlas a mano cada vez que se
        # ejecuta el programa.

    def nueva_nota(self, texto, etiquetas=''):
        '''Crea una nueva nota y la agrega a la lista de notas'''

        n_nota = Nota(texto, etiquetas)
        self.notas.append(n_nota)

        # TODO: Construir este método.

    def _buscar_por_id(self, id_nota):
        '''Buscar la nota con el id dado'''
        # El "_" al comienzo del nombre del método significa que se pretende que
        # este método sea "privado", es decir, que no se utilice desde fuera de
        # este archivo.

        for i in self.notas:
            if id_nota == i.id:
                return i
        return None

        # TODO: Construir este metodo:
        # Debe retornar la nota con el id dado, o None si no existe dicha nota.

    def modificar_nota(self, id_nota, texto):
        '''Busca la nota con el id dado y modifica el texto'''
        # (Este método ya está hecho)
        # Busca la nota por id, usando el método anterior.
        nota = self._buscar_por_id(id_nota)

        # Si lo encontró, actualiza el texto de la nota y retorna True:
        if nota:
            nota.texto = texto
            return True
        # pero si no lo encontró, retorna False:
        return False

    def modificar_etiquetas(self, id_nota, etiquetas):
        '''Busca la nota con el id dado y modifica las etiquetas'''
        nota = self._buscar_por_id(id_nota)
        if nota:
            nota.etiquetas = etiquetas
            return True

        return False
        # TODO: Construir este metodo, parecido al anterior.

    def buscar(self, filtro):
        '''Retorna una lista de todas las notas que coincidan con el filtro 
        dado, en el texto o en las etiquetas'''

        lista_nueva = []
        for nota in self.notas:
            if nota.coincide(filtro):
                lista_nueva.append(nota)
        return lista_nueva

        # TODO: Construir este metodo. Tener en cuenta que puede retornar una
        # lista vacía

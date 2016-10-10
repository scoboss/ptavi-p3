#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Practica 3
"""
from xml.sax.handler import ContentHandler
from xml.sax import make_parser

"""
Creamos clase
"""


class SmallSMILHandler(ContentHandler):
    """
    Inicializamos.
    """
    def __init__(self):
        self.lista = []
        self.dic = {'root-layout': ['width', 'height', 'background-color'],
                    'region': ['id', 'top', 'bottom', 'left', 'right'],
                    'img': ['src', 'region', 'begin', 'dur'],
                    'audio': ['src', 'begin', 'dur'],
                    'textstream': ['src', 'region']}
    """
    El parsel lo llama cuando encuentra la etiqueta.
    """
    def startElement(self, name, attrs):
        if name in self.dic:
            self.atributos = {}
            for item in self.dic[name]:
                self.atributos[item] = attrs.get(item, "")
            self.crear_lista(name, self.atributos)

    """
    Devuelve la lista con las etiquetas encontradas
    """
    def get_tags(self):
        return self.lista

    """
    Creamos una lista segun lo que va encontrando
    """
    def crear_lista(self, nombre, atributos):
        etiqueta = []
        etiqueta.append(nombre)
        etiqueta.append(atributos)
        self.lista.append(etiqueta)
        return self.lista


"""
Para que imprima la lista
"""


def print_list(list):
    for element in list:
        print (element)


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print_list(cHandler.get_tags())

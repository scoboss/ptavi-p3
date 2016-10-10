#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Practica 3

"""
from xml.sax.handler import ContentHandler
from xml.sax import make_parser


class SmallSMILHandler(ContentHandler):
    """
    Inicializamos.
    """
    def __init__(self):
        self.lista_etiquetas = []
        self.dic = {'root-layout': ['width', 'height', 'background-color'],
                    'region': ['id', 'top', 'bottom', 'left', 'right'],
                    'img': ['src', 'region', 'begin', 'dur'],
                    'audio': ['src', 'begin', 'dur'],
                    'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        if name in self.dic:
            dicc = {}
        for item in self.dic[name]:
            dicc[item] = attrs.get(item, "")
        diccname = {name: dicc}
        self.lista_etiquetas.append(diccname)

    """
    Devuelve la lista con las etiquetas encontradas
    """
    def get_tags(self):
        return self.lista_etiquetas

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print (cHandler.get_tags())

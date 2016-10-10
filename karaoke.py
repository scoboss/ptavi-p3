#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import urllib


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.datos = cHandler.get_tags()

    def __str__(self):
        linea = " "
        for elem in self.datos:
            linea = linea + elem[0]
            atributos = elem[1].items()
            for nombre, valor in atributos:
                linea = linea + '\t' + nombre + '=' + '"' + valor + '"'
            linea = linea + '\n'
        return linea

    """
    Para pasar de smil a Json.
    Smil a Json con dump.
    Json a Smil con load.
    """

    def to_json(self, ficherosmil, nuevo=""):
        if nuevo == '':
            nuevo = ficherosmil.split('.')[0] + '.json'
        with open(nuevo, 'w') as fichero_json:
            json.dump(self.datos, fichero_json, sort_keys=True, indent=4)

    def do_local(self):
        for elem in self.datos:
            atributos = elem[1]
            try:
                url = atributos['src']
                if url != "cancion.ogg":
                    filename = url[url.rfind("/") + 1:]
                    data = urllib.request.urlretrieve(url, filename)
                    atributos['src'] = "http://" + data[0]
            except KeyError as e:
                pass


def get_fichero():
    try:
        fich = sys.argv[1]
        return fich
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")


if __name__ == "__main__":
    fichero = get_fichero()
    karaoke = KaraokeLocal(fichero)
    print(karaoke)
    karaoke.to_json(fichero)
    karaoke.do_local()
    karaoke.to_json(fichero, 'local.json')
    print(karaoke)

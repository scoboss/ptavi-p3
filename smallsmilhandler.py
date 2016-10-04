#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Practica 3

"""
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
        def __init__(self):
                self.lista_etiquetas = []
                self.dicc = {'root-layout': ['width' ,'height' ,
                        'background-color'], 
                        'region': ['id', 'top', 'bottom', 'left', 'right'],
                        'img': ['src', 'region', 'begin', 'dur'],
                        'audio': ['src', 'begin', 'dur'],
                        'textstream': ['src', 'region']}

        

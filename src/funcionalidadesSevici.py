import csv
import math 
import folium
from collections import namedtuple

def lee_estaciones(fichero):
    estaciones = []
    with open(fichero, encoding = 'UTF-8') as f:
        next(f)
        for linea in f:
            nombre, numeroBornetas, numeroBornetasVacias, numeroBicisDisponibles, latitud, longitud = linea.split(',')
            nombre = str(nombre)
            numeroBornetas = int(numeroBornetas)
            numeroBornetasVacias = int(numeroBornetasVacias)
            numeroBicisDisponibles = int(numeroBicisDisponibles)
            coordenadas = (float(latitud), float(longitud))
            tupla = (nombre, numeroBornetas, numeroBornetasVacias, numeroBicisDisponibles, coordenadas)
            estaciones.append(tupla)
    return estaciones

def estaciones_bicis_libres():
    pass

def calcula_estaciones():
    pass

def estaciones_cercanas():
    pass

def media_coordenadas():
    pass
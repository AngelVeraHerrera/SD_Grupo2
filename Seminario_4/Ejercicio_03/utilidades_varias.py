# -*- encoding: utf-8 -*-
'''----------------------------------------------------------------------
# Archivo: utilidades_varias.py
#
# Autor: Ángel Vera Herrera
#
# Fecha: 11 de abril de 2015
#
# Versión: v4
#
# Descripción: Módulo que Contiene diversas utilidades universales
#  a todos los programas. Se irá actualizando conforme sea neesario.
#
# Actualizacion: Añadidas funciones para realizar la conexión con 
#  Twitter haciendo uso de su API, y funciones para almacenar y leer
#  información en formato JSON.
'''

__author__ = 'Grupo_02'


''' 
# --- MODULES --------------------------------
'''
import os

import time

import sys

import twitter

import io

import json



''''
# --- FUNCTIONS --------------------------------
'''
# Función para conectarnos haciendo uso de la API de Twitter
# Contine las claves necesarias para realizar la operación
# Pls no usar nuestras claves para fines malignos... =P
def login_twitter():
# Claves para el acceso ---------------------------
    CONSUMER_SECRET = 'dmGCKJL9ixDsEVgtWRhqvcxWiMtUyOgSS9asyOaDQ5eBHx3Ye6'
    CONSUMER_KEY = 'Zmn48mBvITkfCBxbQdaamshRx'
    ACCESS_TOKEN = '3143813369-NMqoPyc4kgJ2KSbg1QHDTzeeTSqmp9tPbIGfKnK'
    ACCESS_TOKEN_SECRET = 'a1F2fxHE1Jh0ywIqjmQ0ulcbKpNuze7QbOFt6OC10yhNU'
    
    auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    api = twitter.Twitter(auth=auth)
    return api

# Función para cargar un archivo en formato JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()

# Función para salvar un archivo en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

# Función que permite limpiar pantalla. Depende del sistema operativo.
def clear():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == ("ce", "nt", "dos"):
		os.system ("cls")

# Función que indica que una opcion es incorrecta.
def opcion_incorrecta():
    clear()
    print '*************************************'
    print '*  Oooops!! ERROR 404 NOT FOUND!!   *'
    print '*  This option does not exist!!     *'
    print '*  You must choose a valid option!  *'
    print '*************************************'
    time.sleep(2)

def pres_to_continue():
    print '************************************'
    print '* Press any key to continue...     *'
    print '************************************'
    raw_input()
    clear()

# Función que permite salir del programa con código de éxito (0) o error (!0)
def exit(i):
    clear()
    if not i:
        print '\n***********************************'
        print '**  Thanks for use the program!  **'
        print '**     Bye!                       **'
        print '***********************************'
    else: print 'FATAL ERROR!!! AUTODESTROYING THE WORLD!!'
    time.sleep(2) 
    clear()
    sys.exit(i)

'''
# Fin Archivo: utilidades_varias.py
'''

# -*- encoding: utf-8 -*-
'''----------------------------------------------------------------------
# Archivo: utilidades_varias.py
#
# Autor: Ángel Vera Herrera
#
# Fecha: 13 de marzo de 2015
#
# Versión: v1
#
# Descripción: Módulo que Contiene diversas utilidades universales
#  a todos los programas. Se irá actualizando conforme sea neesario.
'''

''' 
# --- MODULES --------------------------------
'''
import os

import time

import sys


''''
# --- FUNCTIONS --------------------------------
'''

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

# Función que permite salir del programa con código de éxito (0) o error (!0)
def exit(i):
    clear()
    if not i:
        print '\n***********************************'
        print '**  Thanks for use the program!  **'
        print '**     By!                       **'
        print '***********************************'
    else: print 'FATAL ERROR!!! AUTODESTROYING THE WORLD!!'
    time.sleep(2) 
    clear()
    sys.exit(i)

'''
# Fin Archivo: utilidades_varias.py
'''

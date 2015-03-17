# -*- encoding: utf-8 -*-
'''
--------------------------------------------------------------------------------------------------
# Archivo: E_01_beer.py
#
# Autor: Ángel Vera Herrera, Ana Pastor Sánchez
#
# Fecha: 13 de marzo de 2015
#
# Versión: v3
#
# Descripción: Ejercicio 01, "Botella de Ron"
#  Este programa canta la famosa canción "99 Bottles of beer".
#  Cuenta con varias opciones, como imprimir por pantalla la
#   canción entera, o imprimirlas en un fichero.
#
# Notas de la versión: El programa tiene funcionalidades extras a las solicitadas, como un 
#  menú, uso de clases, tratamiento de ficheros, llamadas al sistema, importar de una 
#  librería creada por ti, etc. Consultamos el incluir o no estas funciones con el docente
#  y le pareció adecuado incluirlas para que veáis algunos aspectos nuevos de Python.
#  Por ese motivo, hay algunas sentencias "pythonianas" como la que controla que se imprima 
#  "bottle" o "bottles" o el control de flujo "switch case" que a lo mejor chocan si las 
#  comparamos con sentencias de otros lenguajes de programación. 
#  ¡Esperamos que os guste y os sirva para aplicar estos aspectos en los próximos programas!
#
# Notas de la canción: Hemos añadido los dos últimos versos que suele tener la canción tradicional =P
--------------------------------------------------------------------------------------------------
'''

''' 
# --- MODULES --------------------------------
'''
import os 

import sys

import re

''''
# --- FUNCTIONS --------------------------------
'''
''''
# Principal Menu -> Print a Menu in the terminal
def intro():
    utilidades_varias.clear() # Clear the terminal
    print '***************************************'
    print '**     "99 BOTTLES OF BEER"  v3      **'
        print '**       by A. Vera & A.Pastor       **'
        print '***************************************'
        print '* Choose an option:                *'
        print '*----------------------------------*'
        print '*  1) Print the song in terminal   *'
        print '*  2) Print the song in a file     *'  
        print '*  3) Exit                         *'
        print '************************************'
        option = int(input('Selection -> '))  # For input
        utilidades_varias.clear()
        if option not in range(1,4):
            utilidades_varias.opcion_incorrecta() # Incorrect option 
    return option 
'''

           
         


# ==========================================================================================>
''' 
# --- MAIN --------------------------------
#
# PRECONDICIONES: No se repiten palabras.
-------------------------------------------
'''

def chainned_words(li_elements):

    li_beg = [word[0] for word in li_elements] 
    li_beg_aux = list(li_beg)

    li_ends = [word[len(word)-1] for word in li_elements] 

    li_result = []

    for i, end_letter in enumerate(li_ends):
        li_res_aux = []
        li_res_aux.append(li_elements[i])
        while (end_letter in li_beg_aux):
            index = li_beg_aux.index(end_letter)
            li_res_aux.append(li_elements[index])
            end_letter = li_ends[index]
            li_beg_aux[index] = ' '
      
        if (len(li_result) < len(li_res_aux)):
            li_result= li_res_aux

        li_beg_aux = list(li_beg)
    return li_result


li_pokemons = open('pokemon.txt','Ur').read().split()

print chainned_words(li_pokemons)
            








        


#li.append(word)
        




















'''
# Fin Archivo: E_01_beer.py
'''

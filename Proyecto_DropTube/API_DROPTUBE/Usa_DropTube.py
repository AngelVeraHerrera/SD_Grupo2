
'''
# --- MODULES --------------------------------
'''
import os 

import sys

import DropTube_API

import utilidades_varias 

''''
# --- FUNCTIONS --------------------------------
'''

# Principal Menu -> Print a Menu in the terminal
def menu():
    option = 0
    while option <1 or option>4:
        utilidades_varias.clear() # Clear the terminal
        print '***************************************'
        print '**     "DropTube Example"  v1        **'     
        print '***************************************'
        print '* Choose an option:                   *'
        print '*-------------------------------------*'
        print '*  1) Video to Dropbox                *'
        print '*  2) List to Dropbox                 *'  
        print '*  3) First video for list to Dropbox *'
        print '*  4) Exit                            *'
        print '***************************************'
        option = int(input('Selection -> '))  # For input
        utilidades_varias.clear()
        if option not in range(1,5):
            utilidades_varias.opcion_incorrecta() # Incorrect option 
    return option 


def VideoToDrop():
    url = raw_input("Introduzca la url del video: \n")
    utilidades_varias.clear()
    DropTube_API.SubeVideo(url)

    	
def ListToDrop():
    url = raw_input("Introduzca la url de la lista: \n")
    utilidades_varias.clear()
    DropTube_API.SubeLista(url)

def FirstToDrop():
    url = input("Introduzca la url de la lista: \n")
    utilidades_varias.clear()
    DropTube_API.SubeDrop(url)

    
# ==========================================================================================>
''' 
# --- MAIN --------------------------------
#
# Load Menu, and save option
#  If option is 4, finish the program (0)
-------------------------------------------
'''

options = {1 : VideoToDrop, 2 : ListToDrop, 3 : FirstToDrop} 
option = menu()

# MAIN LOOP
while option != 4:
    options[option]()
    option = menu()

utilidades_varias.exit(0)
    	

#SubeLista("https://www.youtube.com/playlist?list=PLs_R8vjfJCvYXhuklwGPUlbcrUMItm-WV")


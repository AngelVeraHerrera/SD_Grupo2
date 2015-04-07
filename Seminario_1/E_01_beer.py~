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

import utilidades_varias # Includes several universal utilities 
                         #  that I use in my programs

''''
# --- FUNCTIONS --------------------------------
'''

# Principal Menu -> Print a Menu in the terminal
def menu():
    option = 0
    while option <1 or option>3:
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

''''
# --- CLASSES--------------------------------
'''

# CLASS Bottless_Sing
# Option = 1 -> Terminal
# Option = 2 -> File
class Bottles_Sing():
 
    # Function that print the song in the terminal
    #  The __ indicates that is a private function (or variable)
    #--------------------------------------------------- 
    def __print_terminal(self, verse_1, verse_2): 
        if self.tittle:
            utilidades_varias.clear()
            print '***************************************'
            print '**    "99 BOTTLES OF BEER"  SONG     **'
            print '***************************************\n*\n*'
            utilidades_varias.time.sleep(1)  # Time sleep
            self.tittle = False              # Swap the flag

        utilidades_varias.time.sleep(0.07)
        print '* ', verse_1, '\n* ', verse_2, '*'
    #--------------------------------------------------- 


    # Function that print the song in the file
    #--------------------------------------------------- 
    def __print_file(self, verse_1, verse_2):
        if self.tittle:
            self.archive = open("99_Bottles_Of_Beer_song", "w")
            
            self.archive.write('***************************************\n')
            self.archive.write('**    "99 BOTTLES OF BEER"  SONG     **\n')
            self.archive.write('***************************************\n*\n*\n')
            self.tittle = False
            utilidades_varias.time.sleep(1)

        self.archive.write('* '+verse_1+'\n* '+verse_2+'*\n')
    #-------------------------------------------------- 


    # When a class is instantiated, the class variables are 
    #  initialized. Use __init__ with (self)for this action.
    # In others languages, self is similar to 'this' in a class
    #-------------------------------------------------- 
    def __init__(self):    
        self.tittle = True   # If TRUE, print the song tittle.
        self.__options = {1 : self.__print_terminal, 2 : self.__print_file} # Options
    #-------------------------------------------------- 


    # Function that sings the song
    #-------------------------------------------------- 
    def sing_the_song(self, option):
        o = 'y'
        tittle = True

        # For repeat the song if we go to the store to buy more beer =P
        while o.strip() == 'y':  
            o = ''

            # For repeat the verses of the song while we have beer
            for i in range(99, 0, -1):   
                rest = 'bottle'+('' if i == 1 else 's')
                verse_1 = str(i)+' '+rest+' of beer on the wall, '+str(i)+' '+rest+' of beer.'
                rest = 'bottle'+('' if i-1 == 1 else 's')
                verse_2 = 'Take one down, pass it around, '+str(i-1)+' '+rest+' of beer on the wall...\n'
                self.__options[option](verse_1, verse_2)  # This is a "switch case" in python
       
            # Finish verses
            verse_1 = 'No more bottles of beer on the wall, no more bottles of beer.'
            verse_2 = 'Go to the store and buy some more, 99 bottles of beer on the wall...\n'
            line = '***********************************************************************\n'
            self.__options[option](verse_1, verse_2)
           
            # For to go or not to buy more beer
            print line
            while o.strip() != 'y' and o.strip() != 'n':
                o = raw_input("  Go to the store? (y/n) -> ")

                if o.strip() != 'y' and o.strip() != 'n': 
                    utilidades_varias.opcion_incorrecta()

            print('\n** OK!! **')
            utilidades_varias.time.sleep(1)
            if o.strip() == 'y':  utilidades_varias.clear()
            else: 
                # If the option is use the file, is very important
                #  close the file after finish their use.
                if option == 2: 
                    self.archive.write(line)
                    self.archive.write('< By A.Vera & A.Pastor =P >')
                    self.archive.write('\n*****************************')
                    self.archive.close() 

                    utilidades_varias.clear()
                    print '\n**********************'
                    print '**  File Created!!  **'
                    print '**********************'
                    utilidades_varias.time.sleep(2)       
    #-------------------------------------------------- 


# ==========================================================================================>
''' 
# --- MAIN --------------------------------
#
# Load Menu, and save option
#  If option not is 3, sing the song
#  If option is 3, finish the program (0)
-------------------------------------------
'''
option = menu()

# MAIN LOOP
while option != 3:
    beer_song = Bottles_Sing()           # Instantiated the class
    beer_song.sing_the_song(option)      # Use the class methods
    option = menu()

# Finish the program without error.
# Calling Successful Exit (0)
utilidades_varias.exit(0)


'''
# Fin Archivo: E_01_beer.py
'''

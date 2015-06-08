# -*- encoding: utf-8 -*-

'''
--------------------------------------------------------------------------------------------------
# Archivo: SDL_funciones.py
#
# Autor: �ngel Vera, Ana Pastor, Gonzalo Lamas ,Jose Manuel Mart�nez
#
# Fecha: 8 de junio de 2015
#
# Versi�n: v2
#
# Descripci�n: Se implementan las funciones necesarias para la b�squeda de
#              palabras en una sopa de letras
#
# Notas de la versi�n: Incluye la posibilidad de ejecuci�n como principal para 
#                       realizar pruebas.
--------------------------------------------------------------------------------------------------
'''


''' 
# --- MODULOS --------------------------------
'''
from SDL_data import *


''' 
# --- CONTENEDORES --------------------------------
'''
direcciones = ["Abajo-Arriba", 
               "Arriba-Abajo", 
               "Izquierda-Derecha",
			   "Derecha-Izquierda", 
               "ArribaIzquierda-AbajoDerecha",
               "ArribaDerecha-AbajoIzquierda", 
               "ArribaIzquierda-AbajoDerecha",
			   "AbajoIzquierda-ArribaDerecha",
               "NO ENCONTRADA"]


''' 
# --- FUNCIONES --------------------------------
'''
#
# Busca la coincidencia de la primera letra de una palabra
#  en la sopa, y si la encuentra, realiza una llamada a
#  una funci�n encargada del procesamiento de la b�squeda
#
def buscar_palabra(sopa, palabra) :

    direccion = direcciones[8]
    coord = {}
    salir = False

	#Buscamos de forma secuencial las posiciones en la sopa donde se encuentra
	# la primera letra de la palabra. Si la encontramos, procedemos al an�lisis
	# recursivo desde esa posici�n. 
    for i, fila in enumerate(sopa) :
        for j, letra in enumerate(fila) :
            if salir == False :
                if letra == palabra[0] :
                    coord = {'x': i, 'y': j}
                    direccion = analizar_coordenada(sopa, palabra, coord)

                    if direccion is not direcciones[8] :
                        salir = True
    resultado = {'direccion' : direccion, 'coord' : coord, 'palabra' : palabra}
    return resultado


#
# Llamada a la recursiva. Busca la palabra en todas las direcciones
#  posibles a partir de una posici�n.
#
def analizar_coordenada(sopa,palabra,coord):

    salir = False
    resultado = direcciones[8]
    nueva = palabra[1:]

    for i in range(8) :
        if salir==False :
            resultado = analizar_coordenada_rec(sopa,nueva,coord,i)

            if resultado in direcciones and resultado is not direcciones[8]:
                salir=True

    return resultado


#
# Realiza la b�squeda de la palabra en una direcci�n concreta
#
def analizar_coordenada_rec(sopa,palabra,coord,direccion):
    
    x = coord['x']
    y = coord['y']

    if len(palabra)==0 :
		return direcciones[direccion]

    
    oper_x = { 0 : x+1, 1 : x-1,  2 : x, 3 : x, 4 : x-1, 
                5 : x+1, 6 : x+1, 7 : x-1}

    oper_y = {0 : y, 1 : y, 2 : y+1, 3 : y-1, 4 : y-1, 
                5 : y-1, 6 : y+1, 7 : y+1}
            
    x = oper_x[direccion]
    y = oper_y[direccion]
    coord = {'x' : x, 'y' : y}

    if (x >= 0 and x < len(sopa) and y >= 0 and y < len(sopa[0])) :
        if sopa[x][y] == palabra[0] :
		    return analizar_coordenada_rec(sopa, palabra[1:], coord, direccion)
        else :
            return direcciones[8]
    else :
	    return direcciones[8]


#
# Pone en may�sculas todos los contenedores
#
def upper_all(sopadeletras, palabras) :

    for index, fila in enumerate(sopadeletras) :
        sopadeletras[index] = fila.upper()

    for index, palabra in enumerate(palabras) :
        palabras[index] = palabra.upper() 

#
# Imprime el resultado de la b�squeda
#
def imprimir_resultado(result):

    if result['direccion'] is not direcciones[8] :
        print "*********************************************************************"
        print "**  La palabra: ", result['palabra'], " ha sido encontrada en: "
        print "**  X =  ", result['coord']['x'] 
       	print "**  Y =  ", result['coord']['y']
        print "**  Direccion: ", result['direccion']   
        print "*********************************************************************\n"  
    else :
        print "**********************************************************************"
        print "**  La palabra: ", result['palabra'], " NO ha sido encontrada."
        print "**********************************************************************\n"

def mostrar_sopa(sopa):
    n = len(sopa)
    m = len(sopa[0])
    
    print "   ",

    for j in range(m):
        print " ",j,
    
    print "\n\n",

    for i in range(n):
        print " ",i, " ",
        for j in range(m):
            print sopa[i][j], " ",
        print "\n",

    print "\n\n",

''' 
# --- MAIN --------------------------------
''' #(Para pruebas)
if __name__ == "__main__":
    
    print "*******************************************"
    print "** Prueba de funcionamiento del modulo:  **"
    print "*******************************************"
    upper_all(sopadeletras_1, palabras_localizar)
    for palabra in palabras_localizar :
        resultado = buscar_palabra(sopadeletras_1, palabra)
        imprimir_resultado(resultado)


#============================================================================
#  FIN Fichero: SDL_funciones.py
#============================================================================
















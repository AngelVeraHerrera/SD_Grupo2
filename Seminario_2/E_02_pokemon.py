# -*- encoding: utf-8 -*-
'''
--------------------------------------------------------------------------------------------------
# Archivo: E_02_pokemon.py
#
# Autor: Ángel Vera Herrera, Ana Pastor Sánchez
#
# Fecha: 19 de marzo de 2015
#
# Versión: v1
#
# Descripción: Ejercicio 02, "Trabajando con Pokemon"
#  Este programa, a partir de una lista de palabras, encuentra la lista más larga 
#  posible de palabras encadenadas (la última letra de una palabra coincide con la 
#  primera de la siguiente palabra). 
#
# Notas de la versión: Para probar el programa, se hará uso de una lista de palabras 
#   que se encuentran en el fichero pokemon.txt.
--------------------------------------------------------------------------------------------------
'''


''' 
# --- MODULES --------------------------------
'''
import utilidades_varias


''''
# --- FUNCTIONS --------------------------------
'''

# Principal Menu -> Print a Menu in the terminal
def intro():
    utilidades_varias.clear()  # Clear the terminal
    print '*****************************************'
    print '**  "Chained Words Pokemon Edition!!"  **'
    print '**       by A. Vera & A.Pastor         **'
    print '*****************************************'
    utilidades_varias.pres_to_continue()


'''
 * Cabecera: chainned_words(li_elements)
 * 
 * @param li_elements   Lista de palabras en las que
 *                      vamos a buscar la cadena más 
 *                      larga de encadenadas.
 *
 * @return Cadena más larga de encadenadas. 
 *
 * Notas: No se pueden saltear palabras que comiencen
 *          por la misma letra. Solo se puede probar continue
 *          la primera ocurrencia.
'''
def chainned_words(li_elements):

  # VARIABLES LOCALES
    # Lista con las letras iniciales de cada palabra.
    li_beg = [word[0] for word in li_elements]  

    # Lista con las letras finales de cada palabra.
    li_ends = [word[-1] for word in li_elements] 

    # Lista de inciiales auxiliar 
    li_beg_aux = list(li_beg)  # Muy importante el list()!! Si no, es una referencia.
    li_result = []             # Resultado final

    # Trabajamos mediante la correspondencia del índice con 
    #  la posición en la que se encuentra una palabra.
    for i, end_letter in enumerate(li_ends):
        li_res_aux = []
        li_res_aux.append(li_elements[i])

        while (end_letter in li_beg_aux):
            index = li_beg_aux.index(end_letter)
            li_res_aux.append(li_elements[index])
            end_letter = li_ends[index]
            li_beg_aux[index] = ' '   # Simbolicamente, eliminamos la "palabra"
                                      # con la que hemos comparado.

        # Si el la lista resultante es es más grande que la
        # que tenemos almacenada como reusltado, la almacenamos.
        if (len(li_result) < len(li_res_aux)):
            li_result = list(li_res_aux) 

        li_beg_aux = list(li_beg)  # Tras formar un resultado, recargamos la lista
                                   # auxiliar y continuamos...
    return li_result
           
# ==========================================================================================>
''' 
-------------------------------------------
# --- MAIN --------------------------------
-------------------------------------------
'''
 
intro()

# Abrimos el fichero. Importante la opcion "Ur"
li_pokemons = open('pokemon.txt','Ur').read().split()

print '\n--------------------------------------------------------------------\n'
print ' - '.join(chainned_words(li_pokemons))
print '\n--------------------------------------------------------------------\n'   
utilidades_varias.pres_to_continue()
utilidades_varias.exit(0)         


'''
# Fin Archivo: E_02_pokemon.py
'''

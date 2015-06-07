/*============================================================================
 * Fichero: sopadeletras_funciones.h
 *
 * Autor: �ngel Vera Herrera
 *
 *----------------------------------------------------------------------------
 *
 * \file    sopadeletras_funciones.h
 *
 * \brief   Se incluyen las variables, constantes, registros y funciones 
 *			necesarias para el funcionamiento del programa principal
 *   		sopadeletras_openmpi.
 *
 *=========================================================================
 */

#ifndef SOPADELETRAS_FUNCIONES_H_
#define SOPADELETRAS_FUNCIONES_H_

/**************************************/
/******	LIBRERIAS  ********************/
/**************************************/
#include <mpi.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>


//------ CONSTANTES DEFINIDAS ---------------------

#define NUM_FILAS 10      //Constante que define el numero de filas de la sopa de letras.
#define NUM_COLUMNAS 11   //Constante que define el numero de columnas de la sopa de letras.
#define NUM_PALABRAS 9    //Constante que define el numero de palabras a buscar en la sopa de letras.
//NOTA: El numero de columnas es uno m�s, por el caracter terminador.

//--- DEFINICI�N DE REGISTROS -----------------

struct coordenada  //Estructura que contiene coordenadas referentes a la sopa.
{
	int x = -1;  //Coordenada de fila. Inicializada por defecto a una posici�n inv�lida.
	int y = -1;  //Coordenada de columna. Inicializada por defecto a una posici�n inv�lida.
	int dir = 0;  //Direcci�n en la que se encuentra la palabra. Inicializada por defecto a direcci�n inv�lida.
};


//--- DECLARACI�N DE FUNCIONES -----------------

/*=========================================================================*
 * \function  coordenada buscar_palabra(char[][NUM_COLUMNAS], char* palabra);
 *
 * \brief   Funci�n que busca una palabra, retornando el resultado mediante
 *			un registro.
 *
 * \param   La sopa de letras, y la palabra a buscar.
 *
 * \return  coordenada   Registro que contiene los resultados de la busqueda.
 *                       Si el campo dir del regustro contiene un 0, la 
 *                       busqueda no ha dado resultados.
 *=========================================================================
*/
coordenada buscar_palabra(char[][NUM_COLUMNAS], char* palabra);

/*=========================================================================*
 * \function  int analizar_coordenada(char[][NUM_COLUMNAS], char* palabra, coordenada& coord);
 *
 * \brief   Funci�n llamada a analizar_coordenada_rec(...);
 *			Analiza una coordenada mediante la funcion a la que llama.
 *
 * \param   La sopa de letras, la palabra, y la estructura donde almacenar resultados.
 *
 * \return  int  Entero que representa la direcci�n en la que se encuentra la palabra.
 *           	 Si es 0, no ha encontrado la palabra. Las coordenadas se almacenan en coord.
 *=========================================================================
*/
int analizar_coordenada(char[][NUM_COLUMNAS], char* palabra, coordenada& coord);

/*=========================================================================*
 * \function  int analizar_coordenada_rec(char[][NUM_COLUMNAS], char* palabra, int x, int y, int direccion);
 *
 * \brief   Funcion recursiva que busca una palabra a partir de una posici�n 
 *          dada. Las coordenadas de esa posicion est�n en la estructura coord.
 *
 * \param   Sopa, un puntero del que nos interesa la letra, posiciones x e y, y la direccion.
 *
 * \return  0 si no encuentra la palabra. 1, 2, 3, 4, 5, 6, 7, 8 dependiendo de la direcci�n
 *            en la que se encuentra la palabra. VER COMENTARIOS EN IMPLEMENTACI�N.
 *=========================================================================
*/
int analizar_coordenada_rec(char[][NUM_COLUMNAS], char* palabra, int x, int y, int direccion);

/*=========================================================================*
 * \function  void mostrar_sopa(char[][NUM_COLUMNAS]);
 *
 * \brief   Funcion que imprime por salida estandar la sopa de letras.
 *
 * \param   La sopa de letras
 *
 * \return  void
 *
 *=========================================================================
*/
void mostrar_sopa(char[][NUM_COLUMNAS]);


#endif

/*============================================================================
 * FIN Fichero: sopadeletras_funciones.h
 *=========================================================================
 */
















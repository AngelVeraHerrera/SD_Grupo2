/*============================================================================
 * Fichero: sopadeletras_funciones.cpp
 *
 * Autor: Ángel Vera Herrera
 *
 *----------------------------------------------------------------------------
 *
 * \file    sopadeletras_funciones.h
 *
 * \brief   Se implementan las funciones necesarias para el funcionamiento 
 *  		del programa principal sopadeletras_openmpi.
 *
 *=========================================================================
 */

/**************************************/
/******	LIBRERIAS  ********************/
/**************************************/
#include "sopadeletras_funciones.h"

coordenada buscar_palabra(char sopa[][NUM_COLUMNAS] , char* palabra)
{
   //Variables internas 
	int i, j;  // Para el control de bucles.
	char car_palabra; //Variable para almacenar la letra con la que comienza la palabra.
	coordenada coord;  //Almacena las coordenadas y la dirección.
	bool salir = false; //Flag para salir del bucle de recorrido.

	car_palabra = toupper(palabra[0]);  //Pasamos la primera letra a mayúscula para
		                // evitar posibles errores de insercción y de comparación.
	                    //  Así, se compararán siempre letras mayúsculas.

	//Buscamos de forma secuencial las posiciones en la sopa donde se encuentra
	// la primera letra de la palabra. Si la encontramos, procedemos al análisis
	// recursivo desde esa posición. 
	for (i = 0; i < NUM_FILAS && salir == false; i++)
	{
		for (j = 0; j < NUM_COLUMNAS && salir == false; j++)
		{
			if (sopa[i][j] == car_palabra) //Si encontramos una posición válida...
			{
				coord.x = i;  //Almacenamos la posición
				coord.y = j;  //Almacenamos la posición

				// Analzamos la coordenada.
				coord.dir = analizar_coordenada(sopa, palabra, coord);

				if (coord.dir != 0)
					salir = true;
			}
		}
	}
	return coord;
}

int analizar_coordenada(char sopa[][NUM_COLUMNAS], char* palabra, coordenada& coord)
{
   //-Variables internas
	bool salir = false;  // Flag para salir si se encuentra la palabra.
	int resultado = 0;   // Variable que almacena el resultado de la búsqueda. Ver posibles 
	                     //  resultados en comentarios en implementación de la función recursiva.

	for (int i = 1; (i <= 8) && salir == false; i++)
	{
		resultado = analizar_coordenada_rec(sopa, palabra, coord.x, coord.y, i);  //Llamada al análisis recursivo
		                                                                             // en la dirección indicada por "i".

		if (resultado != 0)  // Si el resultado es distinto de cero, hemos encontrado la palabra.
			salir = true;    // Salimos por tanto de la búsqueda.
	}

	return resultado;
}

int analizar_coordenada_rec(char sopa[][NUM_COLUMNAS], char* palabra, int x, int y, int direccion)
{		
	if (palabra[0] == '\0')  //Si hemos llegado a esta situación, hemos encontrado la palabra.
	{
        //puts("Estoy aqui"); //Depuracion
		return direccion;        //Retronamos la dirección en la que se encuentra la palabra.
	}	

	if ((x >= 0 && x < NUM_FILAS) && (y >= 0 && y < (NUM_COLUMNAS - 1)))  //Si la coordenada es válida (dentro de los limites 
	{																 // de la sopa) entramos en el bloque.	
		if (sopa[x][y] == toupper(palabra[0]))    //Si la letra de la coordenada actual coincide con la letra de la posicion 
		{                                // actual de la palabra seguimos buscando en la misma dirección.

			switch (direccion)  //Segun la direccion indicada en la función llamada a la recursiva...
			{
			//-------------------------------------------------------------------------
			/*          Dirección 1: Incremento la fila.
				*               Comprobamos si la palabra está hacia arriba.
				*				Abajo-Arriba
			----*----
				|
				|
			*/
			case 1:
				return analizar_coordenada_rec(sopa, palabra +1, x + 1, y, direccion);
				break;

			//-------------------------------------------------------------------------
			/*         Dirección 2: Decremento la fila.
				|            Comprobamos si la palabra está hacia abajo.
				|			Arriba-Abajo
			----*----
				*
				*
			*/
			case 2:
				return analizar_coordenada_rec(sopa, palabra + 1, x - 1, y, direccion);
				break;

			//-------------------------------------------------------------------------
			/*         Dirección 3: Incremento en la columna.
				|            Comprobamos si la palabra está hacia la derecha.
				|			Izquierda-Derecha
			----*****
				|
				|
			*/
			case 3:
				return analizar_coordenada_rec(sopa, palabra +1, x, y + 1,  direccion);
				break;

			//-------------------------------------------------------------------------
			/*         Dirección 4: Decremento en la columna.
				|            Comprobamos si la palabra está hacia la izquierda.
				|			 Derecha-Izquierda
			*****----
				|
				|
			*/
			case 4:
				return analizar_coordenada_rec(sopa, palabra +1 , x, y - 1, direccion);
				break;

			//-------------------------------------------------------------------------
			/*         Dirección 5: Decremento en la columna y fila.
			  * |            Comprobamos si la palabra está hacia arriba a la izquierda.
			   *|			 ArribaIzquierda-AbajoDerecha
			----*----
				|
				|
			*/
			case 5:
				return analizar_coordenada_rec(sopa, palabra +1, x - 1, y - 1,  direccion);
				break;

			//-------------------------------------------------------------------------
			/*         Dirección 6: Decremento en la columna, incremento en fila.
				|            Comprobamos si la palabra está hacia abajo a la izquierda.
				|            ArribaDerecha-AbajoIzquierda
			----*----
			   *|
			 *  |
			*/
			case 6:
				return analizar_coordenada_rec(sopa, palabra + 1, x + 1, y - 1, direccion);
				break;

			//-------------------------------------------------------------------------
			/*         Dirección 7: Incremento en la columna y fila.
				|            Comprobamos si la palabra está hacia abajo a la drecha.
				|			ArribaIzquierda-AbajoDerecha
			----*----
				|*
				| *
			*/
			case 7:
				return analizar_coordenada_rec(sopa, palabra + 1, x + 1, y + 1,  direccion);
				break;

			//-------------------------------------------------------------------------
			/*         Dirección 8: Incremento en la columna y decremento en fila.
				|   *       Comprobamos si la palabra está hacia arriba a la drecha.
				| *			AbajoIzquierda-ArribaDerecha
			----*----
				|
				|
				*/
			case 8:
				return analizar_coordenada_rec(sopa, palabra + 1, x - 1, y + 1,  direccion);
				break;

			default: return 0;  //Caso por defecto
			}
		}
	}
	return 0;   //Si estamos fuera del bloque, o no hemos encontrado coincidencias, retornamos 0.
}

void mostrar_sopa( char sopa[][NUM_COLUMNAS] )
{
   //-Variables internas
	int i, j; // Para el control de bucles.

	printf("   ");

	for (j = 0; j<NUM_COLUMNAS - 1; j++)
		printf(" %d ", j);

	printf("\n\n");

	for (i = 0; i<NUM_FILAS; i++)
	{
		printf(" %d ", i);

		for (j = 0; j<NUM_COLUMNAS; j++)
			printf(" %c ", sopa[i][j]);

		printf("\n");
	}

	printf("\n\n");
}


/*============================================================================
 * FIN Fichero: sopadeletras_funciones.cpp
 *=========================================================================
 */















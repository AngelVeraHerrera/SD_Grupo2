/////////////////////////////////////////////////////////////////////////// o   o
//********* SOPA DE LETRAS EN OPENMPI  *************************////    o
//*******************************************************************//   
//***************************************************************//        
// * @(#) sopadeletras_openmpi.cpp                         ***/////////////
// *                                                      ***//       o
// * @author Ángel Vera Herrera                          ***//     o   o
// *                                                    ***//
// * @version 1.3 26/04/2014                           ***//        o
//*******************************************************//        o oo
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ o
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
///////////////////////////////////////////////////////////////////
*/

/**************************************/
/******	LIBRERIAS  ********************/
/**************************************/

#include "sopadeletras_funciones.h"

using namespace std;

//**********************************************************//
//******** FUNCION MAIN  ***********************************//
//**********************************************************//
int main(int argc, char *argv[])
{
  //- Variables -----------------
	int myrank;         //Identificador del proceso.
	int num_procesos;   //Número de procesos
    int tag = 1;        //Etiqueta
	int resultado[3];  //Para almacenar los 3 datos necesarios para el resultado.
					   // La coordenada "x", la "y" y la dirección respectivamente.
    
	char mensaje[NUM_COLUMNAS + 1];     //Para pasar las palabras a los procesos esclavos.
    char palabra[NUM_COLUMNAS + 1];      // Para almacenar la palabra por parte de los esclavos.
    const char* palabras[NUM_PALABRAS];  //Almacena la lista de palabras a buscar.
    char sopa[NUM_FILAS][NUM_COLUMNAS];  //Sopa que poseen todos los procesos sin información.
	
	int i, j; // Para el control de bucles.

   //Información de estado.
	MPI_Status status;  

   //Inicializa el entorno MPI
    MPI_Init(&argc, &argv);      
   
   //Número de identificación del proceso
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank); 

   //Número total de procesos  
    MPI_Comm_size(MPI_COMM_WORLD, &num_procesos); 

   //INICIO E INICIALIZACIÓN DE ELEMENTOS

	if (myrank == 0)  //Si soy el proceso maestro...
	{
	  //-Variables internas inicializadas, solo conocidas por el proceso maestro.
		char sopadeletras[NUM_FILAS][NUM_COLUMNAS] = {  //SOPA DE LETRAS DADA DE EJEMPLO EN CLASE
			{ "amigosghis" },
			{ "abcdefghaj" },
			{ "abcholomij" },
			{ "abcdofghij" },
			{ "amundlghib" },
			{ "abcdemahio" },
			{ "aicdufghib" },
			{ "ascnopahia" },
			{ "abddefghhn" },
			{ "aoabbaposd" } };

        // Array con todas las palabras que hay que buscar en la sopa de letras. Se ha añadido una palabra que NO está.
		const char* palabras_local[NUM_PALABRAS] = {"hola", "mundo", "amigo", "sopa", "boba", "si", "ni", "mas", "inventada"};

		std::cout << "\n\n**********************************************\n"
        	   	      << "**   Programacion Paralela y Distribuida    **\n"
			          << "**********************************************\n"
			          << "**  PRACTICA 4: Sopa de letras con OpenMPI  **\n"
			          << "**********************************************\n"
			          << "**      Autor: Angel Vera Herrera           **\n"
		    	      << "**********************************************\n";
		getchar();
		
		//Copiamos las palabras a la variable loca, para luego distribuirla.
		for (i = 0; i < NUM_PALABRAS; i++)
			palabras[i] = palabras_local[i]; 

		//Copiamos la sopa de letras inicializada a la variable loca, para luego distribuirla.
		for (i = 0; i < NUM_FILAS; i++)
			for (j = 0; j < NUM_COLUMNAS; j++)
				sopa[i][j] = toupper(sopadeletras[i][j]); //Pasamos a mayúsculas todo.

		std::cout << "\n****************************************\n"
        	   	      << "** SOPA A RESOLVER:                   **\n"
			          << "****************************************\n\n";
		getchar();

		mostrar_sopa(sopa);  //Mostramos por pantalla la sopa que vamos a resolver.
		
		std::cout << "Palabras a buscar: \n\n";  //Mostramos las palabras a buscar.

		for (i = 0; i<NUM_PALABRAS; i++)
			std::cout << palabras[i] << " ";
		
		std::cout << "\n\n";
		getchar();
	} // Fin Inicio

	//Barrera para comenzar el cálculo paralelo de forma sincronizada.
	MPI_Barrier(MPI_COMM_WORLD); //Más que nada la uso para que los flujos de salida estandar no aparezcan 
								 // desordenados en pantalla en diversas situaciones. Se puede omitir.

	//Realizamos un broadcast, enviando la sopa de letras. Los esclavos la reciben.
	MPI_Bcast(sopa, NUM_FILAS*NUM_COLUMNAS, MPI_CHAR, 0, MPI_COMM_WORLD); 

   //DISTRIBUCIÓN DE TAREAS

	if(myrank == 0) //Si soy el proceso maestro...
	{
      //-Variables internas del maestro
		int trabajos = NUM_PALABRAS;         //Numero de palabras
		int num_esclavos = num_procesos -1;  //Numero de esclavos
		int pal_proc[num_esclavos];          //Relación esclavos-tarea -> pal_proc[identificador esclavo] almacena el 
											 // numero de palabra asignada.

		const char* direcciones[] = {   //Direcciones en las que se pueden encontrar las palabras.
			"Abajo-Arriba",
			"Arriba-Abajo",
			"Izquierda-Derecha",
			"Derecha-Izquierda",
			"ArribaIzquierda-AbajoDerecha",
			"ArribaDerecha-AbajoIzquierda",
			"ArribaIzquierda-AbajoDerecha",
			"AbajoIzquierda-ArribaDerecha" };

		//cout<<"Numero Procesos:"<<num_procesos<<endl;    //Depuración
		//cout<<"Numero Esclavos:"<<num_esclavos<<endl;    //Depuración

		std::cout << "******************************************************\n"
        	   	      << "** Resultados obtenidos de la busqueda de palabras: **\n"
			          << "******************************************************\n\n";
		getchar();
		j = 0;  //Almacena por que palabra vamos.

	  //- Asignamos tareas iniciales a los procesos.
		for (i = 0; i<num_esclavos && trabajos != 0; i++)
		{    
            strcpy (mensaje,palabras[j]);
			MPI_Send(mensaje, strlen(mensaje)+1, MPI_CHAR, i + 1, tag, MPI_COMM_WORLD);
			trabajos--;
            pal_proc[i+1] = j; // Relacionamos el proceso con la palabra que le ha sido enviada.
			j++;               //Incrementamos el contador de palabras.
            //cout<<mensaje<<endl;  //Depuración
		}
		
		while(trabajos != 0)  //Mientras tengamos tareas pendientes...
		{
		   // Recibimos el resultado.
			MPI_Recv(resultado, 3, MPI_INT, MPI_ANY_SOURCE, tag, MPI_COMM_WORLD, &status);

		   //Imprimimos el resultado.
            //cout<<resultado[0]<<endl;  //Depuracion
			//cout<<resultado[1]<<endl;  //Depuracion
			//cout<<resultado[2]<<endl;  //Depuracion

			std::cout << "Resultado del proceso "<<status.MPI_SOURCE<<"\n\n";

			if (resultado[2] != 0)  // Si la palabra ha sido encontrada...
			{
				std::cout << "La palabra <<"<<palabras[pal_proc[status.MPI_SOURCE]]<<">> ha sido encontrada en: \n";
            	std::cout << "X =  " << resultado[0] << "\n";
            	std::cout << "Y =  " << resultado[1] << "\n";
				std::cout << "Direccion: "<<direcciones[resultado[2] - 1] <<  "\n\n\n";
			}
            else
				std::cout << "La palabra "<<palabras[pal_proc[status.MPI_SOURCE]]<<" NO ha sido encontrada. \n\n\n";
			
			//Enviamos la siguiente tarea al proceso libre y realizamos la relación.
            strcpy (mensaje,palabras[j]);
			MPI_Send(mensaje, strlen(mensaje)+1, MPI_CHAR, status.MPI_SOURCE, tag, MPI_COMM_WORLD);
			pal_proc[status.MPI_SOURCE] = j; //Relación.

			j++;          // Pasamos a la siguiente palabra.
			trabajos --;  // Decrementamos el número de trabajos.
		}

		while( num_esclavos != 0)  //Cuando se ha acabado el numero de trabajos, esperamos la finalización de los esclavos.
		{
		   // Recibimos el resultado.
			MPI_Recv(resultado, 3, MPI_INT, MPI_ANY_SOURCE, tag, MPI_COMM_WORLD, &status);

		   //Imprimimos el resultado.
            //cout<<resultado[0]<<endl;  //Depuracion
			//cout<<resultado[1]<<endl;  //Depuracion
			//cout<<resultado[2]<<endl;  //Depuracion

			std::cout << "Resultado del proceso "<<status.MPI_SOURCE<<"\n\n";

			if (resultado[2] != 0)  // Si la palabra ha sido encontrada...
			{
				std::cout << "La palabra <<"<<palabras[pal_proc[status.MPI_SOURCE]]<<">> ha sido encontrada en: \n";
            	std::cout << "X =  " << resultado[0] << "\n";
            	std::cout << "Y =  " << resultado[1] << "\n";
				std::cout << "Direccion: "<<direcciones[resultado[2] - 1] <<  "\n\n\n";
			}
            else
				std::cout << "La palabra "<<palabras[pal_proc[status.MPI_SOURCE]]<<" NO ha sido encontrada. \n\n\n";
			
			num_esclavos--; //Decrementamos el numero de esclavos trabajando.
		}

	   //Para finalizar, enviamos a todos los procesos esclavos la señal de fin, para que dejen de trabajar.
		strcpy(mensaje, "FIN");

		for (i = 1; i < num_procesos; i++) 
			MPI_Send(mensaje, strlen(mensaje) + 1, MPI_CHAR, i, tag, MPI_COMM_WORLD);

		std::cout << "\n\n**********************************************\n"
           	      << "**         FIN DE LA EJECUCION              **\n"
		          << "**********************************************\n\n";
		getchar();
	} //Fin proceso maestro
	
	else  //Si NO soy el proceso maestro... (soy un esclavo)
	{
	   // -Variables del proceso
		coordenada res;  // Almacena los resultados.

       //Obtenemos la palabra a buscar.
    	MPI_Recv(palabra,  NUM_COLUMNAS + 1, MPI_CHAR, 0, tag, MPI_COMM_WORLD, &status);
		
		//puts(palabra);
	
		while(strcmp(palabra, "FIN") != 0 )   //Mientras no nos llegue la señal de parada...
		{
			res = buscar_palabra(sopa, palabra);   //Buscamos la palabra en la sopa.
          
           //Almacenamos los resultados.
			resultado[0] = res.x;
			resultado[1] = res.y;
			resultado[2] = res.dir;
			
           //Enviamos los resultados, y obtenemos una nueva palabra para buscar (o la señal de fin).
			MPI_Send(resultado, 3, MPI_INT, 0, tag, MPI_COMM_WORLD);
            MPI_Recv(palabra, NUM_COLUMNAS + 1, MPI_CHAR, 0, tag, MPI_COMM_WORLD, &status);
			//puts(palabra);
		}
        //puts("He salido"); //Depuración
	}// Fin proceso esclavo

   //Finaliza el entorno MPI
    MPI_Finalize();
}

/*============================================================================
 * FIN Fichero: sopadeletras_openmpi.cpp
 *=========================================================================
 */







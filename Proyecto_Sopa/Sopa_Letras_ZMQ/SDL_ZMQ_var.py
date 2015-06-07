DIR_IP_PUSH = "tcp://127.0.0.1:5557"
DIR_IP_PULL = "tcp://127.0.0.1:5558"
DIR_IP_CONTROL = "tcp://127.0.0.1:5559"
NUM_ESCLAVOS = 3
NUM_PALABRAS = 9
END_FLAG = "FINISHED"

sopadeletras_1 = ["amigosghis",
                  "abcdefghaj",
			      "abcholomij",
			      "abcdofghij",
			      "amundlghib",
			      "abcdemahio",
    		      "aicdufghib",
    	          "ascnopahia",
			      "abddefghhn",
			      "aoabbaposd"]

palabras_localizar = ["hola", "mundo", "amigo", "sopa", "boba", 
                          "si", "ni", "mas", "inventada"]

direcciones = ["Abajo-Arriba", 
               "Arriba-Abajo", 
               "Izquierda-Derecha",
			   "Derecha-Izquierda", 
               "ArribaIzquierda-AbajoDerecha",
               "ArribaDerecha-AbajoIzquierda", 
               "ArribaIzquierda-AbajoDerecha",
			   "AbajoIzquierda-ArribaDerecha"]

def upper_all() :

    for index, fila in enumerate(sopadeletras_1) :
        sopadeletras_1[index] = fila.upper()

    for index, palabra in enumerate(palabras_localizar) :
        palabras_localizar[index] = palabra.upper() 


def imprimir_resultado(result):
    print 'Resultado del proceso: ', result['worker']

    if result['encontrada'] :
        print "La palabra: ", result['palabra'], " ha sido encontrada en: "
        print "X =  ", result['coor']['x'] 
       	print "Y =  ", result['coor']['y']
        print "Direccion: ", result['direccion']     
    else :
        print "La palabra: ", result['palabra'], " NO ha sido encontrada."








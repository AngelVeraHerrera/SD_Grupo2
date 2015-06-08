
# -*- encoding: utf-8 -*-

'''
--------------------------------------------------------------------------------------------------
# Archivo: SDL_ZMQ.py
#
# Autor: Ángel Vera, Ana Pastor, Gonzalo Lamas ,Jose Manuel Martínez
#
# Fecha: 8 de junio de 2015
#
# Versión: v4
#
# Descripción: 
    El sistema completo permite repartir entre diversos nodos distribuidos las palabras
     que hay que localizar en una sopa de letras, dividiendo de esta forma el trabajo. 
     Hace uso de paradigmas de la programación distribuida.

    En este fichero se encuentran los tres componentes que por separado componen
       un sistema distribuido basado en ZMQ. Por una parte, el "ventilator" enviará
       las tareas al pool de trabajo. Para ello, primero enviará a todos la sopa, y
       a continuación enviará los trabajos (las palabras a buscar). Por otra parte,
       el "worker" haciendo uso de la libreria SDL_funciones, realizará la búsqueda
       de la palbra correspondiente y retornará un resultado al "result_manager". Este 
       último componente es precisamente el encargado de la recogida y publicación de
       resultados.

    En un sistema real, estos tres componentes estarían en ejecución por separado. Para
       evitar tener que realizar pruebas de esta forma, se ha obtado por la creación de 
       procesos paralelos mediante las utilidades del módulo multiprocessing. Se creará
       un proceso correspondiente a un "ventilator", otro para el "result_manager", y una
       número determinado de "workers" definido en la constante NUM_WORKERS.

    De esta forma, con la simple interpretación (Python 2.7) de este fichero, se 
        recreará un proceso paralelo y distribuido de programación. También se han
        llevado a cabo pruebas distribuidas en diferentes computadores, resultando
        estas en éxito.
#
# Notas de la versión: Incluye la posibilidad de ejecución como principal para 
#                       realizar pruebas.
--------------------------------------------------------------------------------------------------
'''

''' 
# --- MODULOS --------------------------------
'''
import time
import zmq
from  multiprocessing import Process
from SDL_data import *
from SDL_funciones import *
from utilidades_varias import *
''' 
# --- CONSTANTES --------------------------------
'''
NUM_WORKERS = 4
NUM_PALABRAS = 9
DIR_IP_PUSH = "tcp://127.0.0.1:5557"
DIR_IP_PULL = "tcp://127.0.0.1:5558"
DIR_IP_CONTROL = "tcp://127.0.0.1:5559"
END_FLAG = "FINISHED"

''' 
# --- FUNCIONES --------------------------------
'''
#
# VENTILATOR
#
def ventilator():
      
    # Convertimos a mayúsculas (para mejor visualización)
    sopadeletras = sopadeletras_1
    upper_all(sopadeletras, palabras_localizar)

    # Mostramos la sopa de letras.
    mostrar_sopa(sopadeletras)

    # Inicializamos el contexto zeromq
    context = zmq.Context()

    # Creamos el canal para el envío de trabajos
    ventilator_send = context.socket(zmq.PUSH)
    ventilator_send.bind(DIR_IP_PUSH)

    time.sleep(1) # spin up and connect

    # Distribuimos la sopa de letras a todos los procesos
    for worker in range(NUM_WORKERS) :
        ventilator_send.send_json(sopadeletras)

    # Publicamos las palabras a localizar
    for palabra in palabras_localizar :
        ventilator_send.send_json(palabra)

    print "******************************************"
    print "** TRABAJO ENVIADO DESDE EL VENTILATOR  **"
    print "******************************************\n"
    time.sleep(1)


#
# WORKER
#
def worker(wrk_num):

    # Inicializamos el contexto zeromq
    context = zmq.Context()

    # Creamos el canal para obtener trabajo del "ventilator"
    work_receiver = context.socket(zmq.PULL)
    work_receiver.connect(DIR_IP_PUSH)

    # Creamos un canal para reportar los resultados al "result_manager"
    results_sender = context.socket(zmq.PUSH)
    results_sender.connect(DIR_IP_PULL)

    # Creamos un canal para obtener los mensajes de control del "result_manager"
    control_receiver = context.socket(zmq.SUB)
    control_receiver.connect(DIR_IP_CONTROL)
    control_receiver.setsockopt(zmq.SUBSCRIBE, "")

    # Configuramos un poller para multiplexar los canales 
    #  del receptor del receptor de trabajo y de control
    poller = zmq.Poller()
    poller.register(work_receiver, zmq.POLLIN)
    poller.register(control_receiver, zmq.POLLIN)

    sopa_flag = False
    sopa_local = []

    # Aceptaremos mensajes hasta que a partir de un mensaje de control
    #  finalicemos.
    while True:

        socks = dict(poller.poll())

        if socks.get(work_receiver) == zmq.POLLIN:
            if sopa_flag == False :
                sopa_local = work_receiver.recv_json()
                sopa_flag = True

            else :
                # Obtenemos la palabra a buscar, la procesamos y realizamos la 
                #  búsqueda, y publicamos los resultados.
                palabra = work_receiver.recv_json()                
                resultado = buscar_palabra(sopa_local, palabra)                

                # Añadimos al resultado el número de trabajador que lo ha obtenido
                # y procedemos al envío.
                resultado["worker"] = wrk_num
                results_sender.send_json(resultado)
                
        # SI el mensaje de control corresponde al definido para abortar, 
        #  cerramos el worker.
        if socks.get(control_receiver) == zmq.POLLIN:
            control_message = control_receiver.recv()
            if control_message == "FINISHED":
                print "****************************************************"
                print "**  Worker %i ha finalizado todas sus tareas!!" % wrk_num
                print "****************************************************\n"
                break


#
# RESULT_MANAGER
#
def result_manager():

    # Inicializamos el contexto zeromq
    context = zmq.Context()

    # Creamos un canal para obtener los resultados
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind(DIR_IP_PULL)

    # Creamos un canal para enviar los mensajes de control
    control_sender = context.socket(zmq.PUB)
    control_sender.bind(DIR_IP_CONTROL)

    # Recogemos los resultados de todos los trabajadores
    # y los publicamos
    for task_nbr in range(len(palabras_localizar)) :
        result = results_receiver.recv_json()   
        print '***********************************************'
        print "** Resultado del worker", result["worker"]    
        imprimir_resultado(result)
        
    # Signal to all workers that we are finsihed
    control_sender.send("FINISHED")
    time.sleep(5)

if __name__ == "__main__":
    clear()
    # Create a pool of workers to distribute work to
    worker_pool = range(NUM_WORKERS)
    for wrk_num in range(len(worker_pool)):
        Process(target=worker, args=(wrk_num,)).start()
    
    # Fire up our result manager...
    result_manager = Process(target=result_manager, args=())
    result_manager.start()

    # Start the ventilator!
    ventilator = Process(target=ventilator, args=())
    ventilator.start()







# -*- encoding: utf-8 -*-

''' 
# --- MODULOS --------------------------------
'''
import time
import zmq
from  multiprocessing import Process
from SDL_data import *
from SDL_funciones import *


NUM_WORKERS = 3
NUM_PALABRAS = 9
DIR_IP_PUSH = "tcp://127.0.0.1:5557"
DIR_IP_PULL = "tcp://127.0.0.1:5558"
DIR_IP_CONTROL = "tcp://127.0.0.1:5559"
END_FLAG = "FINISHED"


def ventilator():
      
    upper_all(sopadeletras_1, palabras_localizar)

    sopadeletras = sopadeletras_1
  
    
    # Initialize a zeromq context
    context = zmq.Context()

    # Set up a channel to send work
    ventilator_send = context.socket(zmq.PUSH)
    ventilator_send.bind(DIR_IP_PUSH)

    # Give everything a second to spin up and connect
    time.sleep(1)

    # Distribuimos la sopa de letras a todos los procesos
    for worker in range(NUM_WORKERS) :
        ventilator_send.send_json(sopadeletras)

    for palabra in palabras_localizar :
        ventilator_send.send_json(palabra)

    print "TRABAJO ENVIADO DESDE EL VENTILATOR\n"
    time.sleep(1)



# The "worker" functions listen on a zeromq PULL connection for "work" 
# (numbers to be processed) from the ventilator, square those numbers,
# and send the results down another zeromq PUSH connection to the 
# results manager.

def worker(wrk_num):

    # Initialize a zeromq context
    context = zmq.Context()

    # Set up a channel to receive work from the ventilator
    work_receiver = context.socket(zmq.PULL)
    work_receiver.connect(DIR_IP_PUSH)

    # Set up a channel to send result of work to the results reporter
    results_sender = context.socket(zmq.PUSH)
    results_sender.connect(DIR_IP_PULL)

    # Set up a channel to receive control messages over
    control_receiver = context.socket(zmq.SUB)
    control_receiver.connect(DIR_IP_CONTROL)
    control_receiver.setsockopt(zmq.SUBSCRIBE, "")

    # Set up a poller to multiplex the work receiver and control receiver channels
    poller = zmq.Poller()
    poller.register(work_receiver, zmq.POLLIN)
    poller.register(control_receiver, zmq.POLLIN)

    sopa_flag = False
    sopa_local = []

    # Loop and accept messages from both channels, acting accordingly
    while True:

        socks = dict(poller.poll())

        if socks.get(work_receiver) == zmq.POLLIN:
            if sopa_flag == False :
                sopa_local = work_receiver.recv_json()
                sopa_flag = True

            else :
                palabra = work_receiver.recv_json()
                
                resultado = buscar_palabra(sopa_local, palabra)                

                resultado["worker"] = wrk_num
          
                results_sender.send_json(resultado)
                
        # If the message came over the control channel, shut down the worker.
        if socks.get(control_receiver) == zmq.POLLIN:
            control_message = control_receiver.recv()
            if control_message == "FINISHED":
                print("Worker %i apagando!" % wrk_num)
                break


# The "results_manager" function receives each result from multiple workers,
# and prints those results.  When all results have been received, it signals
# the worker processes to shut down.
def result_manager():

    # Initialize a zeromq context
    context = zmq.Context()

    # Set up a channel to receive results
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind(DIR_IP_PULL)

    # Set up a channel to send control commands
    control_sender = context.socket(zmq.PUB)
    control_sender.bind(DIR_IP_CONTROL)

    for task_nbr in range(len(palabras_localizar)) :
        result = results_receiver.recv_json()   
        print '***********************************************'
        print "** Resultado del worker", result["worker"]    
        imprimir_resultado(result)
        
    # Signal to all workers that we are finsihed
    control_sender.send("FINISHED")
    time.sleep(5)

if __name__ == "__main__":

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






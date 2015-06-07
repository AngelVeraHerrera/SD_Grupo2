import time
import zmq
from  multiprocessing import Process
from SDL_ZMQ_var import *

# The "ventilator" function generates a list of numbers from 0 to 10000, and 
# sends those numbers down a zeromq "PUSH" connection to be processed by 
# listening workers, in a round robin load balanced fashion.


def ventilator():
      
    upper_all()

    sopadeletras = sopadeletras_1
  
    
    # Initialize a zeromq context
    context = zmq.Context()

    # Set up a channel to send work
    ventilator_send = context.socket(zmq.PUSH)
    ventilator_send.bind(DIR_IP_PUSH)

    # Give everything a second to spin up and connect
    time.sleep(1)

    # Distribuimos la sopa de letras a todos los procesos
    for esclavo in range(NUM_ESCLAVOS) :
        ventilator_send.send_json(sopadeletras)

    for palabra in palabras_localizar :
        ventilator_send.send_json(palabra)

    print "Trabajo enviado"
    time.sleep(1)




# The "worker" functions listen on a zeromq PULL connection for "work" 
# (numbers to be processed) from the ventilator, square those numbers,
# and send the results down another zeromq PUSH connection to the 
# results manager.

def esclavo(wrk_num):

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
                print wrk_num, sopa_local
            else :
                palabra = work_receiver.recv_json()
                print wrk_num,  palabra
                resultado = {'worker' : wrk_num, 
                             'palabra' : palabra, 
                             'encontrada' : True, 
                             'coor' : {'x': 1, 'y': 2}, 
                             'direccion' : direcciones[2]}
          
                results_sender.send_json(resultado)
                
        # If the message came over the control channel, shut down the worker.
        if socks.get(control_receiver) == zmq.POLLIN:
            control_message = control_receiver.recv()
            if control_message == "FINISHED":
                print("Worker %i received FINSHED, quitting!" % wrk_num)
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
        imprimir_resultado(result)
        
    # Signal to all workers that we are finsihed
    control_sender.send("FINISHED")
    time.sleep(5)

if __name__ == "__main__":

    # Create a pool of workers to distribute work to
    worker_pool = range(NUM_ESCLAVOS)
    for wrk_num in range(len(worker_pool)):
        Process(target=esclavo, args=(wrk_num,)).start()
    
    # Fire up our result manager...
    result_manager = Process(target=result_manager, args=())
    result_manager.start()

    # Start the ventilator!
    ventilator = Process(target=ventilator, args=())
    ventilator.start()






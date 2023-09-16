import threading
import time

# Definir un buffer de tamaño limitado
buffer = [] # Esta lista representa nuestro buffer.
buffer_size = 5 # Tamaño máximo del buffer.

# Semáforos para controlar el acceso al buffer
mutex = threading.Semaphore(1)  # Semaforo que actúa como un mutex, para la sección crítica
empty = threading.Semaphore(buffer_size)  # Semaforo que cuenta los espacios vacíos en el buffer.
full = threading.Semaphore(0)  # Semaforo que cuenta los elementos en el buffer.

# Función del productor
def productor():
    global buffer
    while True:
        item = generador_item()  # Esta funcion genera un nuevo elemento
        empty.acquire()  # Decrementar el contador de espacios vacíos
        mutex.acquire()  # Entrar a la sección crítica
        buffer.append(item)  # Agregar el elemento al buffer
        mutex.release()  # Salir de la sección crítica
        full.release()  # Incrementar el contador de elementos en el buffer
        time.sleep(1)  # Simular un proceso de producción

# Función del consumidor
def consumidor():
    global buffer
    while True:
        full.acquire()  # Decrementar el contador de elementos en el buffer
        mutex.acquire()  # Entrar a la sección crítica
        item = buffer.pop(0)  # Consumir el primer elemento del buffer
        mutex.release()  # Salir de la sección crítica
        empty.release()  # Incrementar el contador de espacios vacíos
        process_item(item)  # Procesar el elemento
        time.sleep(1)  # Simular un proceso de consumo

# Funciones de ejemplo
def generador_item():
    return time.time()  # Generar un timestamp como elemento

def process_item(item):
    print(f"Procesando item: {item}")

# Crear y iniciar los hilos
producer_thread = threading.Thread(target=productor)
consumer_thread = threading.Thread(target=consumidor)
producer_thread.start()
consumer_thread.start()
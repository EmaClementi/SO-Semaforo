import threading
import time

# Definir un buffer de tamaño limitado
buffer = []
buffer_size = 5

# Crear un monitor utilizando threading.Condition
class MonitorBuffer:
    def __init__(self):
        self.cond = threading.Condition()
    
    def add_item(self, item): # El método add_item permite al productor agregar un elemento al buffer de manera segura.
        with self.cond: # Esto asegura que el monitor esté bloqueado de manera exclusiva mientras se ejecuta el código dentro del bloque.
            while len(buffer) >= buffer_size: # Verifica si el buffer está lleno. Si lo está, el productor se bloquea esperando.
                self.cond.wait() # Agrega el elemento al buffer.
            buffer.append(item)
            self.cond.notify() # Notifica al consumidor que hay elementos disponibles para consumir.

    def get_item(self):
        with self.cond:
            while len(buffer) == 0: # Verifica si el buffer está vacío. Si lo está, el consumidor se bloquea esperando.
                self.cond.wait()
            item = buffer.pop(0) # Obtiene y remueve el primer elemento del buffer.
            self.cond.notify()
            return item

# Crear una instancia del monitor
monitor = MonitorBuffer()

# Función del productor
def productor():
    while True:
        item = generate_item()  # Generar un nuevo elemento
        monitor.add_item(item)  # Agregar el elemento al buffer
        time.sleep(1)  # Simular un proceso de producción

# Función del consumidor
def consumidor():
    while True:
        item = monitor.get_item()  # Obtener un elemento del buffer
        process_item(item)  # Procesar el elemento
        time.sleep(1)  # Simular un proceso de consumo

# Funciones de ejemplo
def generate_item():
    return time.time()  # Generar un timestamp como elemento

def process_item(item):
    print(f"Procesando item: {item}")

# Crear y iniciar los hilos
producer_thread = threading.Thread(target=productor)
consumer_thread = threading.Thread(target=consumidor)
producer_thread.start()
consumer_thread.start()

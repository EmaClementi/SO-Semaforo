import threading

class BaseDeDatos:
    def __init__(self):
        self.mutex = threading.Condition()
        self.num_lectores = 0

    def leer(self):
        with self.mutex:
            self.num_lectores += 1
            if self.num_lectores == 1:
                self.escritor_bloqueado = True
            print("Lector leyendo")
        
        with self.mutex:
            self.num_lectores -= 1
            if self.num_lectores == 0:
                self.escritor_bloqueado = False
                self.mutex.notify()  # Despierta al escritor si estaba bloqueado

    def escribir(self):
        with self.mutex:
            while self.num_lectores > 0 or self.escritor_bloqueado:
                self.mutex.wait()  # Espera hasta que no haya lectores o escritores
            print("Escritor escribiendo")

# Creamos una instancia de la base de datos
base_de_datos = BaseDeDatos()

# Funciones para simular lectura y escritura
def leer():
    base_de_datos.leer()

def escribir():
    base_de_datos.escribir()

# Creamos varios hilos de lectura y escritura
lectores = []
escritores = []

for i in range(5):
    lector = threading.Thread(target=leer)
    lector.start()
    lectores.append(lector)

for i in range(2):
    escritor = threading.Thread(target=escribir)
    escritor.start()
    escritores.append(escritor)

# Esperamos a que todos los hilos terminen
for lector in lectores:
    lector.join()

for escritor in escritores:
    escritor.join()

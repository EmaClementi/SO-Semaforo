import threading

# Definimos semáforos para controlar el acceso a la base de datos
lectores_sem = threading.Semaphore()
escritores_sem = threading.Semaphore()

# Variable para mantener el número de lectores en ejecución
num_lectores = 0

# Función que simula la lectura de la base de datos
def leer():
    global num_lectores
    with lectores_sem:
        num_lectores += 1
        if num_lectores == 1:
            escritores_sem.acquire()  # Si es el primer lector, bloquea a los escritores
    # Leer de la base de datos
    print("Lector leyendo")
    with lectores_sem:
        num_lectores -= 1
        if num_lectores == 0:
            escritores_sem.release()  # Si no hay más lectores, libera a los escritores

# Función que simula la escritura en la base de datos
def escribir():
    with escritores_sem:
        # Escribir en la base de datos
        print("Escritor escribiendo")

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

import threading
#Importamos la libreria threading que nos permite crear semaforos
# Creamos 2 semaforos y le damos un valor inicial en 0
# El programa permite que los hilos ejecuten las funciones
# y muestren los numeros en orden.
semaforo1 = threading.Semaphore(0)
semaforo2 = threading.Semaphore(0)

def funcion1():
    print(1) 
    semaforo1.release()
    semaforo2.acquire()
    print(3)
    semaforo1.release()

def funcion2():
    semaforo1.acquire()
    print(2)
    semaforo2.release()
    semaforo1.acquire()
    print(4)

threading.Thread(target=funcion1).start()
threading.Thread(target=funcion2).start()

#funcion1:
# Imprime "1".
# Libera (release) semaforo1, incrementando su contador a 1.
# Libera semaforo2, incrementando su contador a 1.
# Imprime "3".
# Libera semaforo1 nuevamente, incrementando su contador a 2.

# funcion2:
# Adquiere (acquire) semaforo1. Dado que inicialmente está en 0, este paso bloqueará el hilo hasta que semaforo1 sea liberado por funcion1.
# Imprime "2".
# Libera semaforo2, incrementando su contador a 1.
# Adquiere semaforo1 nuevamente. Ahora que funcion1 lo ha liberado, este paso tiene éxito y el hilo continúa.
# Imprime "4".

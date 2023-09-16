import threading

class Filosofo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tenedor_izquierdo = threading.Condition()
        self.tenedor_derecho = threading.Condition()
        self.comiendo = False

    def tomar_tenedores(self):
        with self.tenedor_izquierdo:
            with self.tenedor_derecho:
                while self.comiendo:  # Espera activa si está comiendo otro filósofo
                    self.tenedor_izquierdo.wait()
                    self.tenedor_derecho.wait()
                self.comiendo = True

    def dejar_tenedores(self):
        with self.tenedor_izquierdo:
            with self.tenedor_derecho:
                self.comiendo = False
                self.tenedor_izquierdo.notify()  # Notifica a los filósofos vecinos
                self.tenedor_derecho.notify()

def cenar(filosofo):
    while True:
        # Filósofo piensa
        print(f'{filosofo.nombre} está pensando.')

        # Filósofo tiene hambre y quiere comer
        filosofo.tomar_tenedores()

        # Filósofo come
        print(f'{filosofo.nombre} está comiendo.')

        # Filósofo deja los tenedores y vuelve a pensar
        filosofo.dejar_tenedores()

if __name__ == '__main__':
    filosofos = [Filosofo(f'Filósofo {i+1}') for i in range(5)]
    hilos = []

    for filosofo in filosofos:
        hilo = threading.Thread(target=cenar, args=(filosofo,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

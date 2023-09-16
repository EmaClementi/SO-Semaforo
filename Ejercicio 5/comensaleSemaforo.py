import threading

NUM_FILOSOFOS = 5
tenedores = [threading.Lock() for _ in range(NUM_FILOSOFOS)]

def filosofo(i):
    tenedor_izquierdo = tenedores[i]
    tenedor_derecho = tenedores[(i + 1) % NUM_FILOSOFOS]

    while True:
        # Filósofo piensa
        print(f'Filósofo {i} está pensando.')

        # Filósofo tiene hambre
        tenedor_izquierdo.acquire()
        tenedor_derecho.acquire()

        # Filósofo come
        print(f'Filósofo {i} está comiendo.')

        # Filósofo deja los tenedores
        tenedor_izquierdo.release()
        tenedor_derecho.release()

if __name__ == '__main__':
    filosofos = []
    for i in range(NUM_FILOSOFOS):
        filosofo_thread = threading.Thread(target=filosofo, args=(i,))
        filosofo_thread.start()
        filosofos.append(filosofo_thread)

    for filosofo_thread in filosofos:
        filosofo_thread.join()

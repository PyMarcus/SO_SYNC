from threading import Thread, Lock, RLock
from time import sleep
from colorama import Fore


counter: int = 0


class Process(Thread):
    """
    OBJETIVO: utilizar 10 threads em semáforos.

    """

    def __init__(self, process) -> None:
        super().__init__()
        self.process = process

    def run(self) -> None:
        global counter, mutex

        i = 1000
        while i:
            mutex.acquire()
            print(Fore.YELLOW + f"Processo {self.process}, entrou na sessão crítica, contador {counter}")
            counter += 1
            print(Fore.BLUE + f"Processo {self.process} saiu da sessão crítica, contador {counter}")
            i -= 1
            sleep(0.1)
            mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    process = [Process(num) for num in range(10)]        # cria 10 threads
    [proc_instace.start() for proc_instace in process]  # inicializa as 10 threads
    [proc_instace.join() for proc_instace in process]  # termina as threads e continua o código
    print(Fore.GREEN + f"Resultado final do contador: {counter}")  # como são 10 threads, o resultado esperado é 100.
    print(Fore.RESET)

from threading import Thread, Semaphore
from time import sleep
from colorama import Fore


counter: int = 0
sem: Semaphore = Semaphore(1)


class Process(Thread):
    """
     OBJECTIVE: use 10 threads in semaphores.

    Traffic lights are variables that control the
    execution of the threads preventing the critical session problem.

    So what it does is prevent a thread from executing a
    operation while another is running.
    """

    def __init__(self, process) -> None:
        super().__init__()
        self.process = process

    def run(self) -> None:
        global counter, sem

        while True:
            sem.acquire()  # lock the resource for the current thread (Wait)
            print(Fore.YELLOW + f"Processo {self.process}, entrou na sessão crítica, contador {counter}")
            counter += 1
            print(Fore.BLUE + f"Processo {self.process} saiu da sessão crítica, contador {counter}")
            sem.release()  # unlock (Up)
            sleep(1)       # wait 1s


if __name__ == '__main__':

    process = [Process(num) for num in range(10)]  # create 10 threads
    [proc_instace.start() for proc_instace in process]  # initialize the 10 threads

    """
    # for debug
    [proc_instace.join() for proc_instace in process]    # wait unitil threads finished and continue code
    print(Fore.GREEN + f"Resultado final do contador: {counter}")  # como são 10 threads, o resultado esperado é 100.
    print(Fore.RESET)
    """

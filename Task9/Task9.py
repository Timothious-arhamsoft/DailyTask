# Task 1: Concurrency-vs-parallelism concept check, stated out loud


'''
Concurrency:
Managing multiple tasks together by switching between them..

Parallelism:
Running multiple tasks simultaneously on multiple CPU cores.

Threading:
it uses Concurrency

asyncio:
it uses Concurrency

Multiprocessing:
it uses both Concurrency and Parallelism as it provides true parallelism.

'''

# CPU's hardware threads
# Command: lscpu
'''
(Physical Cores:)
Core(s) per socket:      4 
(Threads per Core:)
Thread(s) per core:      2
Socket(s):               1
(Total Logical CPUs:)
CPU(s):                  8
'''

# Task 2: Threaded, I/O-bound
import time
from concurrent.futures import ThreadPoolExecutor

def Seq_task(number):
    print(f"Sequencial Task {number} started")
    time.sleep(1)
    print(f"Sequencial Task {number} finished")

def Thead_task(number):
    print(f"Thread Task {number} started")
    time.sleep(1)
    print(f"Thread Task {number} finished")


# Task 3:  CPU-bound proof

def main():
    # ----> Sequencial
    # seq_start = time.time()
    # for i in range(5):
    #     Seq_task(1)
    # seq_end = time.time()
    # print("Sequencial Time: ", seq_end-seq_start)

    # ----> Thread
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(Thead_task, range(1,6))

    end = time.time()

    print("Thread Time:", end-start)

if __name__ == "__main__":
    main()



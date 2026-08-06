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
#-------------------------
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
#-------------------------

# Task 2: Threaded, I/O-bound
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def Seq_task(number):
    print(f"Sequencial Task {number} started")
    time.sleep(1)
    print(f"Sequencial Task {number} finished")

def Thead_task(number):
    print(f"Thread Task {number} started")
    time.sleep(1)
    print(f"Thread Task {number} finished")


# Task 3:  CPU-bound proof
def cpu_bound_squares(_):
    total = 0

    for i in range(20_000_000):
        total += i*i

    return total

# Task 4: Asyncio
import asyncio
async def asyn_task(n):
    print(f"Asyn Task {n} started")
    await asyncio.sleep(1)
    print(f"Asyn Task {n} Ended")

async def async_main():

    start = time.time()

    await asyncio.gather(
        asyn_task(1),
        asyn_task(2),
        asyn_task(3),
        asyn_task(4),
        asyn_task(5)
    )

    end = time.time()

    print("Async Time:", end - start)

# Task 5: Real HTTP requests
import requests
def http_request():
    url = "https://jsonplaceholder.typicode.com/users/5"
    try:
        response = requests.get(url)
        status = response.status_code
        print("Status Code: ",status)
        if status == 200:
            data = response.json()
            # print(data)
            print("\nUser Details")
            print("Name:", data["name"])
            print("Username:", data["username"])
            print("Email:", data["email"])
            print("City:", data["address"]["city"])
        else:
            print("Request Failed")
    except requests.exceptions.RequestException as e:
        print("Request Error: ",e)


def main():
    # Task 2
    # ----> Sequencial
    # seq_start = time.time()
    # for i in range(5):
    #     Seq_task(i)
    # seq_end = time.time()
    # print("Sequencial Time: ", seq_end-seq_start)

    # ----> Thread
    # start = time.time()
    # with ThreadPoolExecutor(max_workers=5) as executor:
    #     executor.map(Thead_task, range(1,6))

    # end = time.time()

    # print("Thread Time:", end-start)

    # Task 3
    # Cpu Bound
    # cpu_bound_start_time = time.time()
    # for i in range(4):
    #     cpu_bound_squares(i)
    # cpu_bound_end_time = time.time()
    # print("Cpu Bound Time: ", cpu_bound_end_time-cpu_bound_start_time)

    #Thread
    # thread_bound_start_time = time.time()
    # with ThreadPoolExecutor(max_workers=4) as executor:
    #     list(executor.map(cpu_bound_squares, range(4)))
    # thread_bound_end_time = time.time()
    # print("Thread Time: ", thread_bound_end_time-thread_bound_start_time)

    # Multitasking
    # multi_start_time = time.time()
    # with ProcessPoolExecutor() as executor:
    #     list(executor.map(cpu_bound_squares, range(4)))
    # multi_end_time = time.time()
    # print("Multiprocessing Time: ", multi_end_time-multi_start_time)


    # Task 4
    # asyncio.run(async_main())

    #Task 5
    http_request()
if __name__ == "__main__":
    main()



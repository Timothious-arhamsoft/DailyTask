import multiprocessing
from multiprocessing import Pool
def worker(num):
    print(f"Worker: {num}")

def square(x):
    return x * x

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker, args=(1,))
    process.start()
    process.join()
    with Pool(4) as pool:
        print(pool.map(square, [1, 2, 3, 4]))
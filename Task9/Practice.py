import multiprocessing
from multiprocessing import Pool
import requests
def worker(num):
    print(f"Worker: {num}")

def square(x):
    return x * x

def http_request():
    url = "https://jsonplaceholder.typicode.com/posts/5"

    try:
        response = requests.get(url)
        print("Status: ", response.status_code)
   
        data = response.json()
        # print("Data: ",data)
        print("Id:", data["userId"])
        print("Title: ", data["title"])
    except requests.exceptions.RequestException  as e:
        print(e)


if __name__ == "__main__":
    # process = multiprocessing.Process(target=worker, args=(1,))
    # process.start()
    # process.join()
    # with Pool(4) as pool:
    #     print(pool.map(square, [1, 2, 3, 4]))
    http_request()
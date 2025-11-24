import multiprocessing as mp
import time

def worker(arr, value_to_add):
    for i in range(len(arr)):
        arr[i] += value_to_add

def main():
    print(f"Number of CPU cores: {mp.cpu_count()}")

    shared_array = mp.Array('i', [1, 2, 3, 4, 5])
    processes = []
    print(f"Initial shared array: {list(shared_array)}")

    start = time.time()
    for i in range(5):
        p = mp.Process(target=worker, args=(shared_array, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(f"Final shared array: {list(shared_array)}")
    print(f"Time taken: {end - start} seconds")


if __name__ == "__main__":
    main()
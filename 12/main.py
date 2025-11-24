import threading
import time
import urllib.request


def sequential_download(url):
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(f"Downloaded {len(data)} bytes from: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def threaded_download(url):
    try:
        print(f"{threading.current_thread().name}: Downloading {url}")
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(
                f"{threading.current_thread().name}: downloaded {len(data)} bytes from: {url}"
            )
    except Exception as e:
        print(f"{threading.current_thread().name}: Error downloading {url}: {e}")


def main():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
    ]

    start = time.time()
    for url in urls:
        sequential_download(url)
    end = time.time()
    print(f"Sequential download time: {end - start:.2f} seconds")

    start = time.time()
    # manual threading 
    threads = []
    for i, url in enumerate(urls):
        t = threading.Thread(
            target=threaded_download, args=(url,), name=f"Thread-{i + 1}"
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"Threading download time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()

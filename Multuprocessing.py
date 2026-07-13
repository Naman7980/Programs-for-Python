import multiprocessing
import os
import requests


def downloadFile(name, url):
    print(f"started downloading {name}")

    response = requests.get(url)
    open(f"file/files{name}.jpg", "wb").write(response.content)

    print(f"finished downloading {name}")


if __name__ == "__main__":
    os.makedirs("file", exist_ok=True)

    # All of this must be indented inside the if statement
    url = "https://picsum.photos/2000/3000"
    pros = []

    for i in range(50):
        p = multiprocessing.Process(target=downloadFile, args=[i, url])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()


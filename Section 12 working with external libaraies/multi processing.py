# import requests
# import multiprocessing
#
# def downloadFile(url, name):
#     response = requests.get(url)
#
#     with open(f"Files/file{name}.jpg", "wb") as f:
#         f.write(response.content)
#     print(f"Finished downloading {name}")
#
#
# if __name__ == "__main__":
#     multiprocessing.freeze_support()
#
#     pros = []
#     url = "https://picsum.photos/2000/3000"
#
#     for i in range(5):
#         p = multiprocessing.Process(target=downloadFile, args=(url, i))
#         p.start()
#         pros.append(p)
#
#     for p in pros:
#         p.join()
#


import requests
import multiprocessing

def downloadFile(url, name):
    response = requests.get(url)

    with open(f"Files/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished downloading {name}")


if __name__ == "__main__":
    multiprocessing.freeze_support()

    pros = []
    url = "https://picsum.photos/2000/3000"

    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()



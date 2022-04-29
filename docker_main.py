import threading
import time
import os

from certStreamConnector import CertStream
from phocaDocker import Phoca
from sharedStorage import Storage


def main():
    PHOCA_WORKERS = 5
    output_file = "C:\\Users\\novakpav\\Documents\\PhocaCrawler\\phoca_test.txt"
    domainStorage = Storage()
    result_storage = Storage()
    crawled = set()

    cert_stream = CertStream(domainStorage)
    os.system("docker build -t phoca ")

    workers = []
    for _ in range(PHOCA_WORKERS):
        workers.append(threading.Thread(target=Phoca(domainStorage, result_storage, crawled)))
    while True:
        if result_storage.size() > 0:
            with open(output_file, "a") as out:
                res = result_storage.pop()
                out.write(res)
                out.write('\n')

if __name__ == "__main__":
    main()
import subprocess
import threading
from asyncio import sleep

import docker


import phoca_main as p


class Phoca(threading.Thread):

    def __init__(self, domain_storage, output_storage, crawled):
        self.domain_storage = domain_storage
        self.output_storage = output_storage
        self.crawled = crawled

    def run(self):
        while True:
            if self.domain_storage.size() == 0:
                sleep(1)
                continue
            domain = self.domain_storage.pop()
            if domain in self.crawled:
                continue
            self.crawled.add(domain)
            result = subprocess.check_output(f"docker run --rm phoca {domain}")
            self.output_storage.push(result)


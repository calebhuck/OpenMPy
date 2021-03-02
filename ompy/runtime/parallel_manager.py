#from threading import *
from ompy.runtime.omp_thread import *

class ParallelManager:
    def __init__(self):
        self.num_threads = 1
        self.threads = None

    def set_num_threads(self, num_threads):
        self.num_threads = num_threads
        #self.threads = [OmpThread(x, num_threads=num_threads) for x in range(num_threads)]

    def submit(self, target):
        for i in range(self.num_threads):
            self.threads = [OmpThread(i, num_threads=self.num_threads) for i in range(self.num_threads)]

        for x in self.threads:
            x._target = target
            x.start()

from threading import Thread

class OmpThread(Thread):
    def __init__(self, my_id, num_threads=1):
        super().__init__(name=str(my_id))
        self.my_id = my_id
        self.num_threads = num_threads

    def get_id(self):
        return self.my_id

    def get_num_threads(self):
        return self.num_threads
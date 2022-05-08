import io
import os

class vidFile(object):
    def __init__(self, name):
        self.output = io.open(name, "wb")

    def write(self, imgBuffer):
        self.output.write(imgBuffer)
    
    def flush(self):
        self.output.flush()
        os.fsync(self.output.fileno())
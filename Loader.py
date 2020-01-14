import time
import sys

class Loader():

    def __init__(self, size):
        self.size = size
        self.current = 0

    def loading(self):
        self.current += 1
        percent = int(self.current/self.size *100)
        time.sleep(0.01)
        sys.stdout.write('\rProgress ' + str(percent) + '%')
        sys.stdout.flush()
        if percent == 100:
            print('\nFinished.\n')

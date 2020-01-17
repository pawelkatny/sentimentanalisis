import time
import sys

class Loader():

    def __init__(self, size):
        self.size = size
        self.current = 0

    def loading(self, text = ''):
        self.current += 1
        percent = int(self.current/self.size *100)
        bar = int(round(20 * self.current/self.size))
        time.sleep(0.0001)
        text_bar = '[' + '*'*bar + ' '*(20-bar) + ']'
        sys.stdout.write('\rProcessing data: ' + text_bar + ' - ' + str(percent) + '%')
        sys.stdout.flush()
        if percent == 100:
            print('\nFinished.\n')

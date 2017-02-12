import threading
from lib.logger import *
import lib.utils as utils
import time


class HourlyStats(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        #self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.ctime = None

    def run(self):
        global lock
        global homenet

        while 1:
            self.ctime = int(time.time())
            self.get_pwnage()
            time.sleep(86400)
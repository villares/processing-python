# JDF's timer thread example (from
# https://github.com/jdf/Processing.py-Bugs/issues/217 )

import threading
import time


class Timer(threading._thread):
    def __init__(self, sleep, func):
        """ execute func(params) every 'sleep' seconds """
        self.func = func
        self.sleep = sleep
        threading._thread.__init__(self, name="PeriodicExecutor")
        self.set_daemon(1)

    def run(self):
        while True:
            time.sleep(self.sleep)
            self.func()


def setup():
    global t
    t = Timer(10, do_something)
    t.start()


def do_something():
    print(millis())

# Py Thread by A. Parish https://gist.github.com/aparrish/950545

from threading import Thread
import random
import time


def settings():
    size(400, 400)


def random_wait(max_seconds, callback):
    seconds = random.randrange(max_seconds)
    time.sleep(seconds)
    callback(seconds)


class Sketch(object):
    def setup(self):
        #size(400, 240)
        self.message = "click to start thread"
        self.thread = None

    def draw(self):
        background(255)
        text_align(CENTER, CENTER)
        text_size(32)
        if self.thread and self.thread.is_alive():
            fill(frame_count % 240)
            text("waiting...", width/2, height/2)
        else:
            fill(64)
            text(self.message, width/2, height/2)

    def thread_callback(self, seconds):
        self.message = "waited " + str(seconds) + " seconds"

    def mouse_pressed(self):
        if self.thread and self.thread.is_alive():
            print "thread already running"
            return
        self.thread = Thread(
            target=random_wait, args=(
                10, self.thread_callback))
        self.thread.start()


sketch = Sketch()


def setup(): sketch.setup()
def draw(): sketch.draw()
def mouse_pressed(): sketch.mouse_pressed()

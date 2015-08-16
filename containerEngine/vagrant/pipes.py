# Class to deal with pipes
import os
import sys
import time
from cmd import commandproc


class dpipes:

    def __init__(self, pipePath):
        self.pipePath = pipePath

    def create(self):
        # make a fifo pipe
        if not os.path.exists(self.pipePath):
            os.mkfifo(self.pipePath)

        print """[%s] [Main Thread] Creating named pipe, 
        to listen to incoming commands""" % time.time()
        self.fifo = open(self.pipePath, 'r')

        while True:
            line = self.fifo.readline()[:-1]
            if line:
                print '[%s] Command Recieved: %s' % (time.time(), line)
                # Spawn a new thread and process the argument
                commandproc(line)

            # Wait for 1 seconds now
            time.sleep(1)

    def destroy(self):
        if os.path.exists(self.pipePath):
            os.remove(self.pipePath)

        # TODO: destroy all out pipes created as well.
        # & Kill all threads

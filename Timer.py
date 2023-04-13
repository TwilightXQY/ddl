import time
import numpy as np


class Timer:  # @save
    """define multiple run time"""

    def __init__(self):
        self.times = []
        self.start()

    def start(self):
        """activate the timer"""
        self.tik = time.time()

    def stop(self):
        """stop the timer & save the time in the form"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def avg(self):
        """return the average time"""
        return sum(self.times) / len(self.times)

    def sum(self):
        """return the total time"""
        return sum(self.times)

    def cumsum(self):
        """return the cumulated sum"""
        return np.array(self.times).cumsum().tolist()

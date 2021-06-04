import math


class Segment(object):
    def __init__(self, start, end):
        self.start = min(start, end)
        self.end = max(start, end)
        self.size = math.fabs(start - end)

    def __str__(self):
        return "Segment " + str(self.start) + " " + str(self.end) + " " + "Size: " + str(self.size)


from rules import Rules


class Timer(object):
    def __init__(self):
        self.time = 0
        self.day = 0

    def tick(self) -> bool:
        """ increases the time by one. Returns whether a whole day has passed """
        if self.time >= Rules.ticks_per_day:
            self.time = 0
            self.day += 1
            return True
        else:
            self.time += 1
            return False

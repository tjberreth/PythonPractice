import math

MINUTES_IN_DAY = 24 * 60

class Clock:
    def __init__(self, hour, minute):
        self._minutes = (hour * 60 + minute) % MINUTES_IN_DAY

    def __repr__(self):
        return f'{int(self._minutes / 60):02d}:{self._minutes % 60:02d}'

    def __eq__(self, other):
        return self._minutes == other._minutes

    def __add__(self, minutes):
        self._minutes = (self._minutes + minutes) % MINUTES_IN_DAY
        return self

    def __sub__(self, minutes):
        self._minutes = (self._minutes - minutes) % MINUTES_IN_DAY
        return self

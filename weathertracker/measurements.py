import copy

from measurement import Measurement
from weathertracker.utils.conversion import (
    convert_to_datetime,
    DatetimeConversionException,
)
from collections import defaultdict


class Measurements:


    def __init__(self, measurements=None):
        self.measurements = defaultdict(list) if measurements is None else measurements


    def add(self, measurement):
        timestamp = measurement.timestamp
        try:
            timestamp = convert_to_datetime(timestamp)
        except DatetimeConversionException:
            pass

        if timestamp not in self.measurements.keys():
            tmp = copy.deepcopy(measurement.metrics)
            self.measurements[timestamp].append(tmp)


    def get_metrics(self, timestamp):
        values = self.measurements[timestamp]
        return values



    def get_measurements_from_range(self, time_range):
        result = []
        for time in time_range:
            if self.measurements[time]:
                m = self.get_metrics(time)
                result.append(m)
        return result


    def get_timestamp_range(self, timestamp_A, timestamp_B):
        result = []
        for k,v in sorted(self.measurements.items()):
            if k >= timestamp_A and k <= timestamp_B:
                result.append(k)
        del (result[-1])
        return result


measurements = Measurements()



        





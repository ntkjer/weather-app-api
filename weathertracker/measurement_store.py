from .measurement import Measurement
import measurements as collected
from werkzeug.exceptions import abort
from werkzeug.datastructures import Headers
from flask import json, Response, request


def add_measurement(measurement):
    ts = measurement['timestamp']
    js = json.dumps(measurement)
    resp = Response(js, status=201, mimetype='application/json')
    resp.headers['Location'] = "/measurements/" + ts
    return resp


def save_measurement(m):
    measure = Measurement(m['timestamp'])
    for k, v in m.iteritems():
        if k == 'timestamp':
            pass
        measure.set_metric(k, v)
    collected.measurements.add(measure)
    


def get_measurement(date, measurements):
    try:
        metrics = measurements.get_metrics(date)
        metrics = metrics[0]
        js = json.dumps(metrics)
        resp = Response(js, status=200, mimetype='application/json')
        return resp
    except:
        abort(404)


def query_measurements(start_date, end_date):
    try:
        date_range = collected.measurements.get_timestamp_range(start_date, end_date)
        measurements = collected.measurements.get_measurements_from_range(date_range)
        return measurements
    except:
        abort(404)

from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import abort
from weathertracker.utils.conversion import (
    convert_to_datetime,
    DatetimeConversionException,
)
from measurement_store import (
    add_measurement,
    get_measurement,
    query_measurements,
    save_measurement
)
from utils.validate import validate_measurements
from measurement import Measurement
import measurements as collected


class MeasurementsAPI(MethodView):
    

    def post(self):
        try:
            m = request.get_json()
            if (validate_measurements(m)): 
                timestamp = m['timestamp']
                save_measurement(m)
                return add_measurement(m)
            else:
                return abort(400)
        except:
            return abort(400)


    def get(self, timestamp):
        try:
            timestamp = convert_to_datetime(timestamp)
        except DatetimeConversionException:
            abort(400)
        return get_measurement(timestamp, collected.measurements)

        



        





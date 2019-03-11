from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements


def get_stats(stats, metrics, from_datetime, to_datetime):
    result = []
    all_stats = ["min", "max", "avg"]
    measurements = query_measurements(from_datetime, to_datetime)
    for metric in metrics:
        numbers = aggregate_metric(metric, measurements)
        if len(numbers) != 0:
            if len(stats) == 1 and stats[0] == "all":
                stats = all_stats
            for stat in stats:
                val = compute_stat(stat, numbers)
                tmp = {
                  'metric': metric,
                  'stat' : stat,
                  'value': val
                }
                result.append(tmp)
    return result


def aggregate_metric(key, measurements):
    values = []
    for metrics in measurements:
        for metric in metrics:
            for i, (k, v) in enumerate(metric.items()):
                if k == key:
                    values.append(v) 
    return values


def compute_stat(stat, numbers):
    stat = stat.lower()
    minimum = maximum = average = None
    if stat == "min":
        minimum = get_min(numbers)
        return minimum
    elif stat == "max":
        maximum = get_max(numbers)
        return maximum
    elif stat == "average":
        average = get_avg(numbers)
        return average


def get_min(numbers):
    return min(numbers)


def get_max(numbers):
    return round(max(numbers), 1)


def get_avg(numbers):
    return round(float(sum(numbers) / max((len(numbers)), 1)), 1)


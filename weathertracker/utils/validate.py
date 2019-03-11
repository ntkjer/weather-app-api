

def validate_measurements(measure):
    if not (measure['timestamp']): 
        return False
    else:
        for k, v in measure.iteritems():
            if k == 'timestamp': pass
            elif not (k == 'timestamp'):
                if type(v) == float or type(v) == int: 
                    pass
                elif type(v) == None:
                    return False
                else:
                    return False
    return True



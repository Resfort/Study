import math

def convert_length(value, from_unit, to_unit):

    conversion_factors = {
        'meters': 1.0,
        'centimeters': 100.0,
        'millimeters': 1000.0,
        'kilometers': 0.001
    }

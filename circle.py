import math

def area(r):
    '''Принимает радиус r, возвращает площадь круга.'''
    if not isinstance(r, (int, float)):
        raise TypeError("Invalid type for radius. Expected int or float.")
    return math.pi * r * r

def perimeter(r):
    '''Принимает радиус r, возвращает периметр круга.'''
    if not isinstance(r, (int, float)):
        raise TypeError("Invalid type for radius. Expected int or float.")
    return 2 * math.pi * r

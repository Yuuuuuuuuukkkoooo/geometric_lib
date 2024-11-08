def area(a):
    """Принимает число a, возвращает квадрат числа a"""
    if not isinstance(a, (int, float)):
        raise TypeError("Invalid type for side of square. "
                        "Expected int or float.")
    return a * a


def perimeter(a):
    """Принимает число a, возвращает 4 * a"""
    if not isinstance(a, (int, float)):
        raise TypeError("Invalid type for side of square. "
                        "Expected int or float.")
    return 4 * a

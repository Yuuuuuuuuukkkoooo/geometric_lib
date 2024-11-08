def area(a, b):
    '''
    Возвращает площадь прямоугольника.

        Параметры:
            a (int, float): сторона прямоугольника
            b (int, float): сторона прямоугольника

        Возвращаемое значение:
            a * b: площадь прямоугольника со сторонами a и b.
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Invalid type for rectangle sides. Expected int or float.")
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника.

        Параметры:
            a (int, float): сторона прямоугольника
            b (int, float): сторона прямоугольника

        Возвращаемое значение:
            (a + b) * 2: периметр прямоугольника со сторонами a и b.
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Invalid type for rectangle sides. Expected int or float.")
    return (a + b) * 2

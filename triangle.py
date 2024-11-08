def area(a, h):
    """
    Возвращает площадь треугольника.

        Параметры:
            a (int | float): основание треугольника
            h (int | float): высота треугольника

        Возвращаемое значение:
            float: площадь треугольника со стороной a и высотой h.
    """
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Основание и высота должны "
                        "быть числами (int или float)")
    return a * h / 2


def perimeter(a, b, c):
    """
    Возвращает периметр треугольника.

        Параметры:
            a (int | float): сторона треугольника
            b (int | float): сторона треугольника
            c (int | float): сторона треугольника

        Возвращаемое значение:
            float: периметр треугольника со сторонами a, b и c.
    """
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("Все стороны треугольника "
                        "должны быть числами (int или float)")
    return a + b + c

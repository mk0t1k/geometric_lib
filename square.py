
def area(a):
    '''
    Вычисляет площадь квадрата.
    
    Параметры:
    a (float): длина стороны квадрата
    
    Возвращаемое значение:
    float: площадь квадрата
    
    Пример вызова:
    >>> area(4)
    16
    '''
    assert a > 0, 'semanticly side must be positive'
    return a * a


def perimeter(a):
    '''
    Вычисляет периметр квадрата.
    
    Параметры:
    a (float): длина стороны квадрата
    
    Возвращаемое значение:
    float: периметр квадрата
    
    Пример вызова:
    >>> perimeter(4)
    16
    '''
    assert a > 0, 'semanticly side must be positive'
    return 4 * a

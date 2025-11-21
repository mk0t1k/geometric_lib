def area(a, h): 
    assert a > 0 and h > 0, 'semanticly height and side must be positive'
    return a * h / 2 

def perimeter(a, b, c): 
    assert a > 0, 'semanticly sides must be positive'
    return a + b + c
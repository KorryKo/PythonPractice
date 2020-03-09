room = str(input())
π = 3.14
if room == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    sTriangle = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    print(sTriangle)
elif room == 'прямоугольник':
    a = int(input())
    b = int(input())
    sRectangle = a * b
    print(sRectangle)
elif room == 'круг':
    r = int(input())
    sCircle = π * r ** 2
    print(sCircle)



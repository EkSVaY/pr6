print("Первый прямоугольник")
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

print("Второй прямоугольник")
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

if (x2 == x3 and y2 == y3) or (x2 == x3 and y1 == y4) or \
        (x1 == x4 and y1 == y4) or (x1 == x4 and y2 == y3):
    print("Прямоугольники касаются")

elif (x2 > x3 > x1 and y1 > y3 > y2) and (y1 > y4 > y2 and x2 > x4 > x1) or \
        (x4 > x2 > x1 > x3 and y3 > y1 > y2 > y4):
    print("Один рюкзак лежит внутри другого, не касаясь")

elif x3 > x2 or x1 > x4 or y4 > y1 or y2 > y3:
    print("Прямоугольники лежат вне друг друга, не касаясь")

elif (x3 <= x2 and y1 >= y3 >= y2) or (x3 <= x2 and y1 >= y4 >= y2) or \
        (x2 >= x4 >= x3 >= x1 and y1 >= y4 >= y2) or (x4 >= x1 and y2 <= y4 <= y1) or \
        (x4 >= x1 and y1 >= y3 >= y2) or (x2 >= x4 >= x3 >= x1 and y1 >= y3 >= y2) or \
        (x4 >= x2 and y3 >= y1 >= y4) or (x4 >= x2 and y3 >= y2 >= y4) or \
        (x4 >= x2 >= x1 >= x3 and y3 >= y2) or (x4 >= x2 >= x1 >= x3 and y1 >= y4) or \
        (x4 >= x1 and y3 >= y1 >= y4) or (x4 >= x1 and y3 >= y2 >= y4):
    print("Прямоугольники пересекаются")

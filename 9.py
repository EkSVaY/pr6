import math

x1 = int(input("x1 - "))
y1 = int(input("y1 - "))
r1 = int(input("r1 - "))
x2 = int(input("x2 - "))
y2 = int(input("y2 - "))
r2 = int(input("r2 - "))

if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) > (r1 + r2):
        print("Окружности лежат одна вне другой, не касаясь")

elif math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) == (r1 + r2):
        print("Окружности имеют внешнее касание")

elif (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < r1 and \
            math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + min(r2, r1) == max(r1, r2)):
        print("Окружности имеют внутреннее касание")

elif math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < r1 and \
            math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + min(r2, r1) < max(r1, r2):
        print("Одна окружность лежит внутри другой, не касаясь.")

elif math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < (r1 + r2):
        print("Окружности пересекаются")

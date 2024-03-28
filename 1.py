import math

r = 6.5
a, b = map(int, input().split("x"))

if 2 * r >= math.sqrt(a ** 2 + b ** 2):
    print("Да")
else:
    print("Нет")

a, b = map(int, input().split("x"))
c, d, e = map(int, input().split("x"))

if (d <= a and e <= b) or (c <= b and d <= a) or (c <= a and e <= b):
    print("да")
else:
    print("нет")

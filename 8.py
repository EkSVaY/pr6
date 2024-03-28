import random

a = [x for x in range(1, 200 + 1)]
random.shuffle(a)
a.insert(0, 0)

chose = int(input())

print(a[chose - 1])

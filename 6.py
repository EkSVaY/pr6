n, k, m = map(int, input().split())
amount = n * 2
time = 0

while amount > 0:
    if k < n:
        amount -= k
        time += m
    elif k >= n:
        time = m * 2
        break
print(time)

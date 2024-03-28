k = int(input())

if k % 5 == 0:
    print("да")
elif k % 7 == 0:
    print("да")
elif (k - (((k // 5) - 1) * 5)) % 7 == 0:
    print("да")
elif (k - ((k // 7) * 7)) % 5 == 0:
    print("да")
else:
    print("нет")

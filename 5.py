one, two = input().split("-")
if (int(two[1]) == (int(one[1]) - 2)) or \
        (int(two[1]) == (int(one[1]) + 2)):
    if one[0] == "a" and two[0] == "b":
        print("Верно")
    elif one[0] == "b" and (two[0] == "a" or two[0] == "c"):
        print("Верно")
    elif one[0] == "c" and (two[0] == "b" or two[0] == "d"):
        print("Верно")
    elif one[0] == "d" and (two[0] == "c" or two[0] == "e"):
        print("Верно")
    elif one[0] == "e" and (two[0] == "d" or two[0] == "f"):
        print("Верно")
    elif one[0] == "f" and (two[0] == "e" or two[0] == "g"):
        print("Верно")
    elif one[0] == "g" and (two[0] == "f" or two[0] == "h"):
        print("Верно")
    elif one[0] == "h" and two[0] == "g":
        print("Верно")
    else:
        print("Неверно")
else:
    print("Неверно")

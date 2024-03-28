cell = input()
if cell[0] in "aceg":
    if int(cell[1]) % 2 == 0:
        print("Белая")
    else:
        print("Черная")
elif cell[0] in "bdfh":
    if int(cell[1]) % 2 != 0:
        print("Белая")
    else:
        print("Черная")

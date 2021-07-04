a = int(input())

i = 1
while i <= a:

    if i % 3 != 0:
        print(i, end = ' ')
    else:
        print("X", end = ' ')
    i += 1
a, b, c = input().split()

x = int(a)
y = int(b)
z = int(c)

if x > y:
    if y > z:
        print(z)
    else:
        print(y)

elif y > z:
    if z > x:
        print(x)
    else:
        print(z)

elif z > x:
    if x > y:
        print(y)
    else:
        print(x)

else: # 값이 전부 동일할 경우.
    print(x)
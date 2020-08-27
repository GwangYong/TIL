a = input()
b = int(a, 16) # a의 16진수 값은 b

for i in range(1, 16):
    print("%s*%X=%X" % (a, i, b*i))
a = int(input())

i = 1
sum = 0

while True:
    sum += i
    if sum >= a:
        print(i)
        break

    i += 1
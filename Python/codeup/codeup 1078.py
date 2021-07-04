a = int(input())

i = 0
sum = 0

while i <= a:

    if i % 2 == 0:
        sum += i

    i += 1

print(sum)
n = int(input())
a = input().split()

num = []

for i in range(0, n):
    num.append(int(a[i]))

for i in range(n - 1, -1, -1):
    print(num[i], end = ' ')
    
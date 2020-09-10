n = int(input())
a = input().split()

lst = [0 for i in range(23)]

for i in range(n):
    lst[int(a[i]) -1] += 1

for i in range(0, 23):
    print(lst[i], end = ' ')

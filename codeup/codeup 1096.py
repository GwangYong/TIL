n = int(input())

arr = [[0 for column in range(19)] for row in range(19)]
# 행, 열 19X19

for i in range(n):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

for j in arr:
    for k in j:
        print(k, end = ' ')
    print()


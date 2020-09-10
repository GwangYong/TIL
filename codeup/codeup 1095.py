a = input()
b = input().split()

n = int(a)
arr = []
for i in range(n):
    arr.append(int(b[i]))

m = 23
for i in range(n):
    if m > arr[i]:
        m = arr[i]

print(m)
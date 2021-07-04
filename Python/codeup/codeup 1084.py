r, g, b = input().split()

R = int(r)
G = int(g)
B = int(b)

count = 0
for i in range(R):
    for j in range(G):
        for k in range(B):
            count += 1
            print(i, j, k)

print(count)

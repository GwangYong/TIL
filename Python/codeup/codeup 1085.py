h, b, c, s = input().split()

H = int(h)
B = int(b)
C = int(c)
S = int(s)

print("%.1f MB" % (H*B*C*S/8/1024/1024))
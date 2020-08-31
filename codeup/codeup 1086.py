w, h, b = input().split()

W = int(w)
H = int(h)
B = int(b)

print("%.2f MB" % (W*H*B/8/1024/1024))
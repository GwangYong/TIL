a, b, c = input().split()
sum = 0

print(int(a) + int(b) + int(c))
sum = float((int(a) + int(b) + int(c)) / 3)
round(sum) # 반올림해주는 함수.

print("%.1f" % sum)
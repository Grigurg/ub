x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a = abs(x1 - x2)
b = abs(y1 - y2)
if a == b:
    print('YES')
else:
    print('NO`')

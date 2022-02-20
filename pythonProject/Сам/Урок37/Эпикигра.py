def nod(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        d = y
        y = x % y
        x = d
    return x


a, b, n = map(int, input().split())
while n != 0:
    n = n - nod(a, n)
    if n == 0:
        r = '0'
        print(r)
        break
    n -= nod(b, n)
    if n == 0:
        r = '1'
        print(r)
        break

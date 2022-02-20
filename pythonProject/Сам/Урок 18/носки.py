n, m = map(int, input().split())
n1 = int(n)
a = 0
# n1 = int(n)
# m1 = int(m)
if m == 0:
    print(n)
else:
    while n >= m:
        n = n//m
        a = a + n
    print(a+n1)

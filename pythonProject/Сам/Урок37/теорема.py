def proverka(x):
    for j in range(2, x):
        if x % j == 0:
            return x % j == 0


n = int(input())
i = 3
while i < n:
    i += 1
    if proverka(i):
        z = n - i
        if proverka(z):
            print(i, z)
            break
    else:
        continue

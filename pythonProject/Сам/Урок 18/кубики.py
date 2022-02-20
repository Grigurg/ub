n = int(input())
a = 1
i = 1
count = 0
while a < n:
    a1 = i
    i = i + 1
    a = a1 + i
    count += 1
print(count)

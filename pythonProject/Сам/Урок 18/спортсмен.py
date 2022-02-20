x = int(input())
y = int(input())
count = 1
while x < y:
    x = x + x * 0.1
    count += 1
print(count)

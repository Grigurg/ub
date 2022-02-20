n = int(input())
hour = n // 60
minute = n - hour * 60
while hour > 23:
    hour = hour - 24
print(hour, minute)
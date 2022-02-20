n = int(input())
a = 0
hour = n // 60 // 60
minute = (n - hour * 60 * 60) // 60
sec = (n - hour * 60 * 60) % 60
if hour > 24:
    hour = hour % 24
print(str(hour).rjust(2, '0'), ':', str(minute).rjust(2, '0'), ':', str(sec).rjust(2, '0'), sep='')
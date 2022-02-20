n = int(input())
n = n % 86400
h = n // 3600
m = n % 3600 // 60
s = n % 60
print(h,':',str(m // 10) + str(m % 10),':',str(s // 10) + str(s % 10), sep='')
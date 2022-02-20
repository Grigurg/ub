n = int(input())
if n >= 10 and n <= 99:
    print('Это число двузначное')
if n > 99 and n < 1000:
    print('Это число трёхзначное')


a = 3
b = 6
c = 5
print(a == b or a == c or b == c)
def year(x):
    temp = ''
    for i in x:
        if i not in temp:
            temp += i
    return x != temp


n = str(input())
n = str(int(n) + 1)
while year(n):
    n = str(int(n) + 1)
print(n)

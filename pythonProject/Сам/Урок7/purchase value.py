a = int(input())
b = int(input())
n = int(input())
rub = a * n
kop = b * n
if kop > 99:
    kop1 = kop // 100
    rub1 = rub + kop1
    kop2 = kop % 100
    print(rub1, kop2)
else:
    print(rub, kop)

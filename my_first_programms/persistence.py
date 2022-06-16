# Напишите программу, которая принимает положительное число и возвращает его мультипликативную персистентность,
# то есть количество раз, которое вы должны умножить цифры в числе, пока не достигнете одной цифры.
# Например:
# 39 --> 3, потому что 3*9 = 27 >> 2*7 = 14 >> 1*4 = 4
# 999 --> 4 потому что 9*9*9 = 729 >> 7*2*9 = 126 >> 1*2*6 = 12 >> 1*2 = 2

def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count


print(persistence(39))
print(persistence(999))

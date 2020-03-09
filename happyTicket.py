n = int(input())
n1 = n % 1000
n2 = n // 1000
var1 = n1 // 100
var2 = (n1 % 100) % 10
var3 = (n1 % 100) // 10
var4 = n2 // 100
var5 = (n2 % 100) % 10
var6 = (n2 % 100) // 10
sum1 = var1 + var2 + var3
sum2 = var4 + var5 + var6
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')

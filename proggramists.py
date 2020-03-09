n = int(input())
n2 = n % 10
n3 = n % 100
if 11<=n3<=14:
    print(int(n), 'программистов')
elif n2 == 1 and n != 11 :
    print(int(n), 'программист')
elif (10 < n < 20) or n2 == 0 or (4 < n2 < 10):
    print(int(n), 'программистов')
else:
    print(int(n), 'программиста')

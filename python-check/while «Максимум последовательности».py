n = int(input())
m = int(input())
while n > 0:
    if n < m:
        n = m
        n = int(input())
    if n > m:
        m = n
        n = int(input())
print(m)

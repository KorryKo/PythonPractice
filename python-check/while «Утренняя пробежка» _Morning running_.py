x = int(input())
y = int(input())
n = 1
while x < y:
   x = x + (0.1 * x)
   n += 1
print(n)

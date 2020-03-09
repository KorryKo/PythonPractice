a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(end='\t')
for j in range(c, d + 1):
    print(j,end='\t')
for i in range(a, b + 1):
    print('\n',i , end='\t')
    for k in range(c, d + 1):
        print(i*k,end='\t')

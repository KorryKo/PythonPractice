genom = str(input())
genom = genom.lower()
g = genom.count('g')
c = genom.count('c')
gc = genom.count('g') + genom.count('c')
total = len(genom)
print((gc / total) * 100)
